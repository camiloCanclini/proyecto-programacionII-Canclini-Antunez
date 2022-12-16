from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def principal():
    return render_template("principal.html")


@app.route("/login")
def login():
    return render_template("login_user.html")

@app.route("/user")
def user():
    return render_template("movie_info.html")



