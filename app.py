from flask import Flask, render_template, request
from db import Database

dbo = Database()

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/perform_registration", methods=["post"])
def perform_registration():
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")
    print("performing")

    response = dbo.insert(name, email, password)

    if response:
        return "User Created Successfully"
    else:
        return "User Already Exsist"


app.run(debug=True)
