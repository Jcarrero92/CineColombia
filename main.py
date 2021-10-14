from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("logIn.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html")