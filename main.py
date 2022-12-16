from flask import Flask, render_template, jsonify, Response
from http import HTTPStatus
import json



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

@app.route("/prueba", methods=["GET"])
def get_data():
    with open('Json/cuentas.json') as content:
        usuarios = json.load(content)
    for usuario in usuarios['users']:
        if usuario['username'] == "admin":
            return usuario['username']
        else:
            return Response("{}",HTTPStatus.NOT_EXTENDED)
        

@app.route("/user/upload_movie")
def user2():
    return render_template("user_menu_upload_movie.html")

if __name__ == "__main__":

    app.run(debug=True)
