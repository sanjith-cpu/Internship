from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to my home page"

@app.route("/about")
def about():
    return "About me"

@app.route("/hello<name>")
def hello(name):
    return f"Hello {name}"

@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    result = a + b
    return f"The sum of {a} and {b} is {result}"

if __name__ == "__main__":
    app.run(debug=True)