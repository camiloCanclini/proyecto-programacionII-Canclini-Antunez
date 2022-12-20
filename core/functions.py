from core import app
import json
import urllib.request

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
def getMovies():
    with open ("database/peliculas.json") as json_file:
        return json.load(json_file)
    
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
        comments = {"Username":"", "Comment":""}
        poster = data["Poster"]

        d = dict()
        d ["Id"] = imdbID
        d ["Title"] = titulo
        d ["Plot"] = sinopsis
        d ["Director"] = director
        d ["Genre"] = genero
        d ["Year"] = año
        d ["Poster"] = poster
        d ["Comments"] = [comments]

        def escribir_json(data, filename="database/peliculas.json"):
            with open (filename, "w") as f:
                json.dump(data, f, indent=4)

        with open ("database/peliculas.json") as json_file:
            data = json.load(json_file)
            temp = data["Movies"]
            temp.append(d)

        escribir_json(data)


    return True


def editMovie(nombrePelicula):

        with open ("database/peliculas.json", "r") as f:
            dict = json.load(f)

            for info in dict['Movies']:
                if info['Title'] == nombrePelicula:
                    info["Title"] = "Mono Azul"
                    info ["Plot"] = "La pelicula del tipo que no tenia piernas y ahora es un mono azul...con piernas, epico"
                    info["Director"] = "Enano Bostero"
                    info ["Genre"] = "Infantil"
                    info["Year"] = "2022 vamo messi"
                    
                    print(info)

editMovie("Avatar")


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

def getDirectors():
    with open ("database/peliculas.json") as json_file:
        file = json.load(json_file)
        directorInDB = set()
        print(file)
        for i in file["Movies"]:
            print(i["Director"])
            director = i["Director"]
            if "," in director:
                genres = director.split(",")
                for i in genres:
                    directorInDB.add(i)
                continue
            if director not in directorInDB:
                directorInDB.add(director)
        print(directorInDB)
        prejson = { 'Directors': list(directorInDB) }
        print(dict(prejson))
        return json.dumps(prejson)


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


getMoviesByDirectors("James Cameron")

