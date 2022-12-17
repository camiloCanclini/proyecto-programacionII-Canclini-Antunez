from flask import Flask, render_template, jsonify, Response, request
from http import HTTPStatus
import json
"""
+---------------+
+-- FUNCTIONS --+
+---------------+ 
"""
def searchUserInJson (username, password, path_json):
    with open(path_json) as content:
        usuarios = json.load(content)
        #print(usuarios)
        #print(usuarios["users"][0])
        for i in usuarios['users']:
            if username == i['username'] and password == i['password']:
                print("\nUser: ", username, "Logged successfully\n")
                return True   
        print("\nUser: ", username, "Was not found\n")
        return False
"""
+------------------+
+-- EVENTS FLASK --+
+------------------+ 
"""
app = Flask(__name__)

"""
+-- INDEX PAGE --+
"""
@app.route("/")
def principal():
    return render_template("index.html")
"""
+-- LOGIN USERS --+
"""
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
        return render_template('login.html')
"""

+---------------------+
+-- BOOT APP SERVER --+
+---------------------+ 
"""
if __name__ == "__main__":
    app.run(debug=True)
