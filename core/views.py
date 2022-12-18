from core import app
from flask import render_template, request
from core.functions import *

@app.route("/")
def principal():
    return render_template("public/index.html",)
@app.route("/login")
def login():
    return render_template("public/login.html")
@app.route("/user", methods=['POST'])
def user(): 
    parametros = request.form
    #print("\nLOS PARAMETROS SON: ", parametros,"\n")
    username = parametros['username']
    password = parametros['pass']
    if searchUserInJson(username, password, 'database/cuentas.json'):
        return render_template('users/movie_info.html')
    else:
        return render_template('login_user.html')

@app.route("/user/addMovie", methods=['GET'])
def addMovies():
    parametros = request.args
    print (parametros["id"])
    
    url= addMovie(parametros["id"]) 

    return "<h1>" + url + "</h1>"



@app.route("/user/upload_movie")
def user2():
    return render_template("user_menu_upload_movie.html")