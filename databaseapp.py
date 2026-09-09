import sqlite3
from flask import Flask, render_template
app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/users')
def show_users():
    conn = get_db_connection()
    users = conn.execute("SELECT id, username, password FROM users").fetchall()
    conn.close()

    return render_template('users.html', users=users)

if __name__ == '__main__':
    app.run(debug=True, port = 5000)