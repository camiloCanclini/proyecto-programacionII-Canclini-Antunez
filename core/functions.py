from core import app
import json
import urllib.request

#Buscar usuarios en el JSON que se encuentra en la carpeta database/cuentas.json

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


#Obtener las peliculas que se guardan en el json que se encuentra en la carpeta database/peliculas.json

def getMovies():
    with open ("database/peliculas.json") as json_file:
        return json.load(json_file)

#Obtiene el ID de las peliculas

def getMovieInfoById(IdMovie):
    with open ("database/peliculas.json", "r") as f:
            dict = json.load(f)
            for movie in dict['Movies']:
                if movie['Id'] == IdMovie:
                    #print(movie)
                    return movie                 


#----------------#
#      A B M
#----------------#

#Funcion de añadir peliculas al html ---> movie_info.html

def addMovie(id):
    url_handler = urllib.request.urlopen('http://www.omdbapi.com/?apikey=cf09fe5c&i=' + id)

    for line in url_handler:
        decoder = line.decode()
        data= json.loads(decoder)
        print(type(data))
        print(data)

        imdbID = data["imdbID"]
        titulo = data["Title"]
        sinopsis = data["Plot"]
        director = data["Director"]
        año = data["Year"]
        genero = data["Genre"]
        poster = data["Poster"]

        d = dict()
        d ["Id"] = imdbID
        d ["Title"] = titulo
        d ["Plot"] = sinopsis
        d ["Director"] = director
        d ["Genre"] = genero
        d ["Year"] = año
        d ["Poster"] = poster
        d ["Comments"] = []

        def escribir_json(data, filename="database/peliculas.json"):
            with open (filename, "w") as f:
                json.dump(data, f, indent=4)

        with open ("database/peliculas.json") as json_file:
            data = json.load(json_file)
            temp = data["Movies"]
            temp.append(d)

        escribir_json(data)

    return True


#Funcion de editar la informacion de las peliculas 

def editMovie(IdMovie, newTitle, newPlot, newDirector, newGenre, newYear, newPoster):
    with open ("database/peliculas.json", "r") as f:
        dict = json.load(f)
        for movie in dict['Movies']:
            print(movie)
            if movie['Id'] == IdMovie:
                print("COINCIDENCIA")
                movie["Title"] = newTitle
                movie ["Plot"] = newPlot
                movie["Director"] = newDirector
                movie ["Genre"] = newGenre
                movie["Year"] = newYear
                movie["Poster"] = newPoster
                break                    
                print(movie)
        with open ("database/peliculas.json", "w") as f:
            json.dump(dict, f, indent=4)


#Funcion de eliminar las peliculas

def deleteMovie(IdMovie):
    print("El ID ES",IdMovie)
    with open ("database/peliculas.json", "r") as f:
        dict = json.load(f)
        contVar = 0
        for movie in dict['Movies']:
            print(movie)
            if movie['Id'] == IdMovie:
                print("COINCIDENCIA")
                del dict['Movies'][contVar]
                print(movie)
                break  
            contVar = contVar + 1
        with open ("database/peliculas.json", "w") as f:
            json.dump(dict, f, indent=4)


#-------------------------#
#Funciones de los servicios (services.py)
#-------------------------#

#Obtiene el genero de cada pelicula que fue agregada en la pagina

def getGenres():
    with open ("database/peliculas.json") as json_file:
        file = json.load(json_file)
        genresInDB = set()
        for i in file["Movies"]:
            print(i["Genre"])
            genre = i["Genre"]
            if "," in genre:
                genres = genre.split(",")
                for i in genres:
                    genresInDB.add(i)
                continue
            if genre not in genresInDB:
                genresInDB.add(genre)
        print(genresInDB)
        prejson = { 'Genres': list(genresInDB) }
        print(dict(prejson))
        return json.dumps(prejson)


#Obtiene los diferentes directores que tiene cada pelicula agregada 

def getDirectors():
    with open ("database/peliculas.json") as json_file:
        file = json.load(json_file)
        directorsInDB = set()
        print(file)
        for i in file["Movies"]:
            print(i["Director"])
            director = i["Director"]
            if "," in director:
                genres = director.split(",")
                for i in genres:
                    directorsInDB.add(i)
                continue
            if director not in directorsInDB:
                directorsInDB.add(director)
        print(directorsInDB)
        prejson = { 'Directors': list(directorsInDB) }
        print(dict(prejson))
        return json.dumps(prejson)


#Obtiene los posters de las peliculas agregadas

def getMoviesPoster():
    with open ("database/peliculas.json") as json_file:
        file = json.load(json_file)
        lista = []
        for i in file["Movies"]: 
            if i["Poster"] != "":
                #print(i)
                lista.append(i)
        movieJson = {"Movies": lista}
        #print(json.dumps(movieJson, indent=4))
        return json.dumps(movieJson, indent=4)


getMoviesPoster()


#Obtiene las peliculas agregadas que fueron dirigidas por el mismo director.

def getMoviesByDirectors(directorSearched):
    with open ("database/peliculas.json") as json_file:
        file = json.load(json_file)
        peliculasDirector = []
        for i in file["Movies"]:
            print(i)
            print()
            if i["Director"] == directorSearched:
                peliculasDirector.append(i["Title"])
                movJson = {"Movies": peliculasDirector}
                print(json.dumps(movJson, indent=4))
                
        return peliculasDirector


getMoviesByDirectors()

