from flask import Flask, render_template, request, redirect
from db import Database
import api

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

    response = dbo.insert(name, email, password)

    if response:
        return render_template(
            "login.html", message="Registration Successfully. Kindly login"
        )
    else:
        return render_template("login.html", message="User Already Exsist")


@app.route("/perform_login", methods=["post"])
def perform_login():
    email = request.form.get("username")
    password = request.form.get("password")

    print(email)
    print(password)

    response = dbo.search(email, password)

    if response:
        return redirect("/profile")
    else:
        return render_template("login.html", message="Incorrect Username/Password")


@app.route("/profile")
def profile():
    return render_template("profile.html")


@app.route("/ner")
def NER():
    return render_template("ner.html")


@app.route("/perform_ner", methods=["post"])
def perform_ner():
    text = request.form.get("text")
    response = api.ner(text)
    print(response)
    return "Done"


app.run(debug=True)
