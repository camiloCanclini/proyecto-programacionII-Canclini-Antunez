from core import app

from flask import render_template, request
from core.functions import *

@app.route("/services/get_movies")
def response():
    return getMovies()

@app.route("/services/get_directors")
def response2():
    return getDirectors()

@app.route("/services/get_genres")
def response3():
    return getGenres()

@app.route("/services/get_movieByDirector", methods=['GET'])
def response4():
    nameDirector = request.args('director')
    return getMoviesByDirector()

@app.route("/services/get_movieWithPoster",methods=['GET'])
def response5():

    return getMoviesPoster()
