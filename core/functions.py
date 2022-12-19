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
    
def addMovie(id):
    url_handler = urllib.request.urlopen('http://www.omdbapi.com/?apikey=cf09fe5c&i=' + id)

    for line in url_handler:
        decoder = line.decode()
        data= json.loads(decoder)
        print(type(data))
        print(data)

        titulo = data["Title"]
        sinopsis = data["Plot"]
        director = data["Director"]
        año = data["Year"]
        genero = data["Genre"]
        comments = {"Username":"", "Comment":""}

        d = dict()
        d ["Title"] = titulo
        d ["Plot"] = sinopsis
        d ["Director"] = director
        d ["Genre"] = genero
        d ["Year"] = año
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


#def deleteMovie(nombrePelicula):



        
