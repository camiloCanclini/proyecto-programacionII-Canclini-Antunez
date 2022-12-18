from core import app
from flask import render_template, request
from core.functions import searchUserInJson

@app.route("/")
def principal():
    return render_template("index.html",)
@app.route("/login")
def login():
    return render_template("login.html")
@app.route("/user", methods=['POST'])
def user(): 
    parametros = request.form
    #print("\nLOS PARAMETROS SON: ", parametros,"\n")
    username = parametros['username']
    password = parametros['pass']
    if searchUserInJson(username, password, 'database/cuentas.json'):
        return render_template('movie_info.html')
    else:
        return render_template('login_user.html')
@app.route("/user/upload_movie")
def user2():
    return render_template("user_menu_upload_movie.html")