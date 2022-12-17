from core import app
import json

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
    
