"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """
import random as rd
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf

default_limit = 1000
sys.setrecursionlimit(default_limit*10)


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Caracterizar las reproducciones")
    print("3- Encontrar música para festejar")
    print("4- Encontrar música para estudiar")
    print("5- Estudiar los géneros musicales")
    print("6- Indicar el género musical más escuchado en el tiempo escogido")

def crear_catalogo():
    return controller.crear_catalogo()

def loaddatos(catalogo):
    return controller.loaddatos(catalogo)

def numerocaracteristicasrango(catalogo,cont,minimo,maximo):
    return controller.numerocaracteristicasrango(catalogo,cont,minimo,maximo)

def numerotracksenergydance(catalogo,minenergy,maxenergy,mindance,maxdance):
    return controller.numerotracksenergydance(catalogo,minenergy,maxenergy,mindance,maxdance)

def numerotracksestudiar(catalogo, mininstrum, maxinstrum, mintempo, maxtempo):
    return controller.numerotracksestudiar(catalogo, mininstrum, maxinstrum, mintempo, maxtempo)

def printresults(resultado):
    print("Total of unique tracks in events: " + str(resultado[0]))
    print("\n")
    print("--- Unique track_id ---")
    a = rd.randint(1,resultado[1]["size"])
    b = rd.randint(1,resultado[1]["size"])
    while a == b:
        b = rd.randint(1,resultado[1]["size"])
    c = rd.randint(1,resultado[1]["size"])
    while c == b or c == a:
        c = rd.randint(1,resultado[1]["size"])
    d = rd.randint(1,resultado[1]["size"])
    while d == c or d == b or d == a:
        d = rd.randint(1,resultado[1]["size"])
    e = rd.randint(1,resultado[1]["size"])
    while e == d or e == c or e == b or e == a:
        e = rd.randint(1,resultado[1]["size"])
    c1 = lt.getElement(resultado[1],a)
    c2 = lt.getElement(resultado[1],b)
    c3 = lt.getElement(resultado[1],c)
    c4 = lt.getElement(resultado[1],d)
    c5 = lt.getElement(resultado[1],e)
    print("Track 1: " + c1["track_id"] + " with energy of " + str(c1["energy"]) + " and danceability of " + str(c1["danceability"]))
    print("Track 2: " + c2["track_id"] + " with energy of " + str(c2["energy"]) + " and danceability of " + str(c2["danceability"]))
    print("Track 3: " + c3["track_id"] + " with energy of " + str(c3["energy"]) + " and danceability of " + str(c3["danceability"]))
    print("Track 4: " + c4["track_id"] + " with energy of " + str(c4["energy"]) + " and danceability of " + str(c4["danceability"]))
    print("Track 5: " + c5["track_id"] + " with energy of " + str(c5["energy"]) + " and danceability of " + str(c5["danceability"]))

def printresults2(resultado):
    print("Total of unique tracks in events: " + str(resultado[0]))
    print("\n")
    print("--- Unique track_id ---")
    a = rd.randint(1,resultado[1]["size"])
    b = rd.randint(1,resultado[1]["size"])
    while a == b:
        b = rd.randint(1,resultado[1]["size"])
    c = rd.randint(1,resultado[1]["size"])
    while c == b or c == a:
        c = rd.randint(1,resultado[1]["size"])
    d = rd.randint(1,resultado[1]["size"])
    while d == c or d == b or d == a:
        d = rd.randint(1,resultado[1]["size"])
    e = rd.randint(1,resultado[1]["size"])
    while e == d or e == c or e == b or e == a:
        e = rd.randint(1,resultado[1]["size"])
    c1 = lt.getElement(resultado[1],a)
    c2 = lt.getElement(resultado[1],b)
    c3 = lt.getElement(resultado[1],c)
    c4 = lt.getElement(resultado[1],d)
    c5 = lt.getElement(resultado[1],e)
    print("Track 1: " + c1["track_id"] + " with instrumentalness of " + str(c1["instrumentalness"]) + " and tempo of " + str(c1["tempo"]))
    print("Track 2: " + c2["track_id"] + " with instrumentalness of " + str(c2["instrumentalness"]) + " and tempo of " + str(c2["tempo"]))
    print("Track 3: " + c3["track_id"] + " with instrumentalness of " + str(c3["instrumentalness"]) + " and tempo of " + str(c3["tempo"]))
    print("Track 4: " + c4["track_id"] + " with instrumentalness of " + str(c4["instrumentalness"]) + " and tempo of " + str(c4["tempo"]))
    print("Track 5: " + c5["track_id"] + " with instrumentalness of " + str(c5["instrumentalness"]) + " and tempo of " + str(c5["tempo"]))
    
    
"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalogo = crear_catalogo()
        loaddatos(catalogo)
    
    elif int(inputs[0]) == 2:
        cont=input("Ingrese la característica de contenido deseada: ")
        minimo=float(input("Ingrese el valor minimo de la característica de contenido deseada: "))
        maximo=float(input("Ingrese el valor maximo de la característica de contenido deseada: "))
        resultado = numerocaracteristicasrango(catalogo,cont,minimo,maximo)
        print(resultado)
    
    elif int(inputs[0]) == 3:
        minenergy=float(input("Ingrese el valor minimo deseado de la característica Energy: "))
        maxenergy=float(input("Ingrese el valor maximo deseado de la característica Energy: "))
        mindance=float(input("Ingrese el valor minimo deseado de la característica Danceability: "))
        maxdance=float(input("Ingrese el valor maximo deseado de la característica Danceability: "))
        print("Obteniendo tracks...")
        resultado = numerotracksenergydance(catalogo,minenergy,maxenergy,mindance,maxdance)
        print("Energy is between " + str(minenergy) + " and " + str(maxenergy) + ".")
        print("Danceability is between " + str(mindance) + " and " + str(maxdance) + ".")
        printresults(resultado)
    
    elif int(inputs[0]) == 4:
        mininstrum=float(input("Ingrese el valor minimo deseado del rango para Instrumentalness: "))
        maxinstrum=float(input("Ingrese el valor maximo deseado del rango para Instrumentalness: "))
        mintempo=float(input("Ingrese el valor minimo deseado del rango para el tempo: "))
        maxtempo=float(input("Ingrese el valor maximo deseado del rango para el tempo: "))
        print("Obteniendo tracks...")
        resultado = numerotracksestudiar(catalogo, mininstrum, maxinstrum, mintempo, maxtempo)
        print("Instrumentalness is between " + str(mininstrum) + " and " + str(maxinstrum) + ".")
        print("Tempo is between " + str(mintempo) + " and " + str(maxtempo) + ".")
        printresults2(resultado)

    elif int(inputs[0]) == 5:
        pass

    elif int(inputs[0]) == 6:
        pass
    else:
        sys.exit(0)
sys.exit(0)
