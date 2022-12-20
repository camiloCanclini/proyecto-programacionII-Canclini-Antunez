from core import app

from flask import render_template, request
from core.functions import *


#------------------#
# S E R V I C I O S
#------------------#

# obtener todas las peliculas cargadas

@app.route("/services/get_movies")
def response():
    return getMovies()

# obtener todos los directores cargados

@app.route("/services/get_directors")
def response2():
    return getDirectors()

# obtener todas los generos cargados

@app.route("/services/get_genres")
def response3():
    return getGenres()

# obtener peliculas basadas en un director en especifico "url?name=[nombredeldirector]"

@app.route("/services/get_movieByDirector", methods=['GET'])
def response4():
    print(request.args)
    nameDirector = request.args['name']
    return getMoviesByDirectors(nameDirector)

# obtener todas las peliculas que tengan una imagen cargada

@app.route("/services/get_moviesWithPoster")
def response5():
    return getMoviesPoster()
