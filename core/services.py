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

@app.route("/services/get_movieByDirector")
def response4():
    return getMoviesByDirectors()

@app.route("/services/get_movieWithPoster")
def response5():
    return getMoviesPoster()


