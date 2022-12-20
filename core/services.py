from core import app

from flask import render_template, request
from core.functions import *


#------------------#
# S E R V I C I O S
#------------------#


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
    print(request.args)
    nameDirector = request.args['name']
    return getMoviesByDirectors(nameDirector)

@app.route("/services/get_moviesWithPoster")
def response5():
    return getMoviesPoster()
