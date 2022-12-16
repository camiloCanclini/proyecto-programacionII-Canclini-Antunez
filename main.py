from flask import Flask, render_template, jsonify
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

@app.route("/json")
def get_data():
    handler = open('Json/cuentas.json', 'r', encoding='utf-8')
    data = handler.read()
    file = json.loads(data)
    return jsonify(file)


@app.route("/user/upload_movie")
def user2():
    return render_template("user_menu_upload_movie.html")

if __name__ == "__main__":

    app.run(debug=True)
