from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    title = "Home Page"
    return render_template('index.html', title=title)

@app.route('/login')
def login():
    return render_template('login.html', page_name = "login")

@app.route('/profile')
def profile():
    user_info = {
        'username': 'sk1007',
        'email': 'sanjith.katakam@gmail.com',
        'role': 'student'
    }
    return render_template('profile.html', user = user_info)

if __name__ == '__main__':
    app.run(debug=True)