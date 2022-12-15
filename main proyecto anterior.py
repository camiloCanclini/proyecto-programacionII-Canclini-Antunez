"""
__________________________________________________________________________________
Sistema Cine (Agenda que guarde peliculas en cartelera)
con ticket (Compra candybar y entrada)- [en caso de que quede corto, le 
ponemos una segunda agenda que guarde la info del cliente]
__________________________________________________________________________________
apikey=71066fc3
omdbapi.com <-- esta es la pagina de la API, desde aca podemos probar comandos
En este caso pasamos por la URL el parametro "s", este es el nombre de la pelicula
Para que la URL funcione necesitamos pasar este paremetro
__________________________________________________________________________________
Developers: Agustin Antunez - Canclini Camilo
__________________________________________________________________________________



"""
#Definicion de Librerias, funciones y metodos----------------------------------------------------------    
import json, random
import os
from tkinter import Menu
import functions #Se linkean las funciones del programa
#Comienzo del Programa--------------------------------------------------------------------------------- 
Menu = True         
while (Menu == True):
    os.system('cls||clear') #limpia la pantalla
    print ("\nObtenga su entrada de cine sin salir de su casa!")
    print("Si usted ya es cliente simplemente ingrese su usuario y contraseña.")
    print ("Por favor, seleccione la opcion correspondiente:\n")
    print ("1) Registrarse")
    print ("2) Ingresar")
    print ("3) Salir")
    try:# Si esto tira error se realiza el except, esto se hace por si se ingresa un numero incorrecto 
        optionSelected = int(input("Ingrese una opcion:"))
    except:
        print("Elija de nuevo porfavor...")
        continue
    #----SECCION DE REGISTRO DE USUARIO(FUNCION)-------------------
    if optionSelected == 1:
        functions.registerAccount()
        os.system('cls||clear') #limpia la pantalla
#----MENU PRINCIPAL-------------------
    elif optionSelected == 2:
        emailSession = functions.login(functions.getUsers())
        os.system('cls||clear') #limpia la pantalla

        while True:
            os.system('cls||clear') #limpia la pantalla
            print ("\n---Bienvenido al Sistema de Cine---")
            print ("---Email de la sesion:",emailSession,"---")
            print ("-Elija una opción a continuación---")
            print ("1) Ver peliculas en cartelera")
            print ("2) Salir")
            try:
                option2Selected = int(input("-> ")) 
            except:
                print("Elija de nuevo porfavor...")
                continue
            os.system('cls||clear') #limpia la pantalla
#----SE MUESTRA LA CARTELERA-------------------
            if option2Selected==1:
                print("\nPeliculas en Cartelera:\n")
                movies = functions.billboardMovies()
                for i in movies.keys():
                    try:
                        print (i,")",end="")
                        print (movies[i]["titulo"])
                        print (movies[i]["fecha"])
                        print (movies[i]["horarios"])
                        print (movies[i]["Genero"])
                        print (movies[i]["Calificacion"])

                    except:
                        continue
#----SELECCION DE PELICULA-------------------
                print("Elija la pelicula(numero)...")
                try:
                    movieNumber = input("-> ") 
                except:
                    print("Elija de nuevo porfavor...")
                    continue

#----SE BUSCA LA PELICULA EN EL JSON-------------------
                for i in movies.keys():
                    if movieNumber == i:
                        movieName = movies[i]["titulo"]
                        print ("pelicula encontrada")
                        break
                if "movieName" not in globals(): #Si el for anterior falla...
                    print("La pelicula no fue encontrada...")
                    continue
                os.system('cls||clear') #limpia la pantalla
#----CANTIDAD DE TICKETS-------------------                
                try:
                    numberTickets = int(input("\nIngrese cantidad de tickets \n-> "))
                except:
                    print("Error al pedir los tickets, vuelva a intentar...")
                    continue
                if numberTickets>10:
                    print ("Usted a requisado demasiados tickets (Maximo 10) ")
                    continue #vuelve a las opciones
                if numberTickets<=0:
                    print ("Usted tiene que seleccionar por lo menos un ticket ")
                    continue #vuelve a las opciones
                price = functions.calcPrice(numberTickets)
                os.system('cls||clear') #limpia la pantalla
#----SELECCION DE ASIENTOS-------------------                
                print ("A continuacion se le presentara matriz con los lugares disponibles")
                seatPlace=functions.seatSearch(numberTickets)
                os.system('cls||clear') #limpia la pantalla 
                print (seatPlace)
#----SE HACE RESUMEN DE LA COMPRA-------------------
                functions.purchaseResume(movieName, numberTickets, price, emailSession)
                print ("Ingrese Y para confirmar, Cualquier otra tecla para cancelar")
                confirmation = input("->")
#----CONFIRMACION DE LA COMPRA-------------------            
                if confirmation == "Y":
                    os.system('cls||clear') #limpia la pantalla
#----SE IMPRIMEN LOS TICKETS
# -------------------            
                    functions.ticketPrint(movieName, seatPlace, movies[movieNumber]["horarios"], movies[movieNumber]["fecha"])
                    print ("Muchas gracias por confiar en nosotros")
                    input("Presione ENTER para continuar...")
                    print ("Volviendo al menu")
                    continue
                else:
                    break
            if option2Selected ==2:
                #print ("Volviendo Al Menu Principal...")
                Menu = False
                break

    elif optionSelected == 3 :
        break           
    
