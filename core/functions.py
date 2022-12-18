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
        print(titulo)

        sinopsis = data["Plot"]
        print(sinopsis)

        director = data["Director"]
        print(director)

        año = data["Year"]
        print(año)

        genero = data["Genre"]
        print(genero)

        d = dict()
        d ["Title"] = titulo
        d ["Plot"] = sinopsis
        d ["Director"] = director
        d ["Genre"] = genero
        d ["Year"] = año
        d ["Comments"] = dict()

        print(d)

        with open ("database/peliculas.json", "a") as f:
            json.dump(d, f, indent=4)
            
    return True


    
        
