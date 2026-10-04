import sqlite3
from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__, template_folder='templates2')
app.secret_key = 'secretkey'


# Helper function to run database queries
def db_query(query, args=(), fetchone=False, fetchall=False, commit=False):
  conn = sqlite3.connect('notes_app.db')
  c = conn.cursor()
  c.execute(query, args)
  res = None
  if commit:
    conn.commit()
  elif fetchone:
    res = c.fetchone()
  elif fetchall:
    res = c.fetchall()
  conn.close()
  return res


@app.route('/')
def index():
  if 'user_id' in session:
    return redirect(url_for('notes'))
  return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
  if request.method == 'POST':
    try:
      db_query(
          'INSERT INTO users (username, password) VALUES (?, ?)',
          (request.form['username'], request.form['password']),
          commit=True,
      )
      return redirect(url_for('login'))
    except sqlite3.IntegrityError:
      return 'Username already taken. Try again.'
  return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    user = db_query(
        'SELECT id FROM users WHERE username = ? AND password = ?',
        (request.form['username'], request.form['password']),
        fetchone=True,
    )
    if user:
      session['user_id'] = user[0]
      return redirect(url_for('notes'))
    return 'Invalid credentials. Try again'
  return render_template('login.html')


@app.route('/notes')
def notes():
  if 'user_id' not in session:
    return redirect(url_for('login'))

  user_notes = db_query(
      'SELECT content FROM notes WHERE user_id = ?',
      (session['user_id'],),
      fetchall=True,
  )
  return render_template('notes.html', notes=user_notes)


@app.route('/add_note', methods=['POST'])
def add_note():
  if 'user_id' in session:
    db_query(
        'INSERT INTO notes (user_id, content) VALUES (?, ?)',
        (session['user_id'], request.form['content']),
        commit=True,
    )
  return redirect(url_for('notes'))


@app.route('/logout')
def logout():
  session.clear()
  return redirect(url_for('login'))


if __name__ == '__main__':
  app.run(debug=True)