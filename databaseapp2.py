from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__, template_folder='Templates')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username,password))
        user = cursor.fetchone()

        conn.close()
        if user:
            return "Login Successful"
        else:
            return "Login Unsuccessful"
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
