import json, random
def billboardMovies():
    jsonFile = open("json/peliculasCartelera.json")
    data = json.load(jsonFile) # Se hace la conversion de la respuesta a Json
    #print(type(data))
    jsonFile.close()
    return data
def calcPrice(numberTickets):
    IVA = 1.21
    priceTicket = 300
    return (priceTicket*numberTickets)*IVA

#FUNCION DEFINIR ASIENTOS
def seatSearch(numberTickets):
    from random import randint
    seatPlace = list()
    print("{:>3}".format("|"), end=" ")
    for x in range(0,12):
        print ("{:<3}".format(x), end = " ")
    print ("")
    print("--------------------------------------------------")
    
    matriz = {"A":[],"B":[],"C":[],"D":[],
            "E":[],"F":[],"G":[],"H":[],
            "I":[],"J":[],"K":[],"L":[]}

    for i in matriz.keys():
        for j in matriz.values():
            j.append(randint(0,1))

    #Resultado
    for i in matriz.keys():
        print (i,"|",end=" ")
        for j in matriz[i]:
            print(j, end="   ")
        print("")
    print ("")
    print ("{:>28}".format("Pantalla"))

    print("")

    #SELECCION DE ASIENTOS
    for n in range(0,numberTickets):
        fila, columna = input("Seleccione un asiento: ")
        columna = int(columna)
        for i in matriz.keys():
            for j in range(0,12):
                if fila == i and columna == j:
                    if matriz[i][j] == 1:
                        print ("Ocupado, seleccione otro")
                        continue
                    elif matriz[i][j] == 0:
                        matriz[i][j] = 1
                        print ("Asiento reservado")
                        seatPlace.append([i,str(j)]) 
                        print("")
    print("{:>3}".format("|"), end=" ")
    return seatPlace

def templateJsonFile():# Esta funcion limpia el JSON y crea el usuario admin
    templateJsonUsers = {
        0:{
            "name": "administratorAccount",
            "email": "admin",
            "password": "admin"}
        } 
    jsonString = json.dumps(templateJsonUsers)
    jsonFile = open("json/cuentas.json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()
def purchaseResume(movieName, numberTickets, price, mailAccount):
    widthLine = "{:^30}" # esto es para que...print("{:^50}".format("...")
    print(widthLine.format("_______Resumen de la Compra_______"))
    print(widthLine.format("Pelicula: "+movieName)) 
    print(widthLine.format("------------------------"))
    print(widthLine.format("Cantida de tickets: "+str(numberTickets))) 
    print(widthLine.format("------------------------"))
    print(widthLine.format("Precio Total (IVA incluido): $"+str(price))) 
    print(widthLine.format("------------------------"))
    print(widthLine.format("Mail de la cuenta: "+mailAccount))
    print(widthLine.format("_________________________________"))
def ticketPrint(movieName, seatPlace, movieDate, movieSchedule):
    ticketCode = "CODE"
    widthLine = "{:^30}" # esto es para que...print("{:^50}".format("...")
    for i in range(0,10):
        ticketCode += str(random.randint(0,9))
    for i in seatPlace:#por cada asiento selecionado se imprime un ticket diferente
        print(widthLine.format("_____________Ticket_____________"))
        print(widthLine.format("CODIGO DE TICKET: "+ticketCode)) 
        print(widthLine.format("------------------------"))
        print(widthLine.format("Pelicula: "+movieName)) 
        print(widthLine.format("------------------------"))
        print(widthLine.format("Asiento: "+str(i[0])+str(i[1]))) 
        print(widthLine.format("------------------------"))
        print(widthLine.format("Fecha: "+movieDate)) 
        print(widthLine.format("------------------------"))
        print(widthLine.format("Horario: "+movieSchedule)) 
        print(widthLine.format("_________________________________"))  
def login(usersData):
    while True:
        emailSession = None
        usuario = input ("\nEmail: ")
        contraseña_ingreso = input ("Contraseña: ")
        for i in usersData.values():
            #print(i)
            if usuario == i["email"] and contraseña_ingreso == i["password"]:
                emailSession = i["email"]
                break       
        if emailSession == None:
            print ("\nUsuario y/o contraseña no validos")
        else:
            break
    return emailSession
def registerAccount():
    name = input ("Nombre Y Apellido: ")
    email = input ("Email: ")
    while True:
        dni = (input ("DNI: "))
        if len(dni) > 10:
            print ("Demasiados caracteres")
        else:
            break
    #Verificacion de contraseña
    repeticion = 3
    while repeticion > 0:
        password = input ("Ingrese una contraseña: ")
        if len(password) < 8:
            print ("Debe ingresar minimo 8 caracteres")
            continue
        else:
            flag = input ("ingrese nuevamente la contraseña: ")

            if password == flag:
                break
            elif repeticion == 0:
                print ("Se acabaron los intentos")
                break
            else: 
                print ("ERROR. Las contraseñas no coinciden")
                repeticion -= 1
                print ("Le quedan", repeticion, "intentos")
    idAccount=""
    while True:
        for i in range(0,4):
            idAccount += str(random.randint(1,9))
            #print(idAccount)
        jsonFile = open('json/cuentas.json')
        usersRegistered = json.load(jsonFile)
        if usersRegistered.get(idAccount) == None:
            usersRegistered [idAccount] = {
                "name": name,
                "email": email,
                "password": password,
                "dni": dni
                }
            #print (usersRegistered)
            jsonString = json.dumps(usersRegistered)
            jsonFile = open("json/cuentas.json", "w")
            jsonFile.write(jsonString)
            jsonFile.close()
            #print (usersRegistered)
            break
        else:
            print ("el id ya existe")
def getUsers():
    jsonFile = open("json/cuentas.json")
    data = json.load(jsonFile)
    return data
#print(getUsers())
