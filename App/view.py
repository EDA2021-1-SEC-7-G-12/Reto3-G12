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
from DISClib.ADT import map as mp
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

def loadgeneros(catalogo):
    return controller.loadgeneros(catalogo)

def numerocaracteristicasrango(catalogo,cont,minimo,maximo):
    return controller.numerocaracteristicasrango(catalogo,cont,minimo,maximo)

def numerotracksenergydance(catalogo,minenergy,maxenergy,mindance,maxdance):
    return controller.numerotracksenergydance(catalogo,minenergy,maxenergy,mindance,maxdance)

def numerotracksestudiar(catalogo, mininstrum, maxinstrum, mintempo, maxtempo):
    return controller.numerotracksestudiar(catalogo, mininstrum, maxinstrum, mintempo, maxtempo)

def tracksgeneros(catalogo,listabusqueda):
    return controller.tracksgeneros(catalogo,listabusqueda)

def datoshoras(catalogo,hora_min,hora_max):
    return controller.datoshoras(catalogo,hora_min,hora_max)

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
    
def printgeneros(tracksgeneros,catalogo):
    print("Total of reproductions: " + str(lt.getElement(tracksgeneros,1)))
    print("\n")
    for x in range(2,lt.size(tracksgeneros)+1):
        datosgenero = lt.getElement(tracksgeneros,x)
        nombre = datosgenero[0]
        minmax = mp.get(catalogo["mapageneros"],nombre)["value"]
        print("======== " + nombre  + " ========")
        print("For " + nombre + " the tempo is between " + str(minmax[0]) + " and " + str(minmax[1]) + " BPM")
        print(nombre + " reproductions: " + str(datosgenero[1][0])+ " with " + str(datosgenero[1][1]) + " different artists.")
        print("----- Some artists for " + nombre + " -----")
        for y in range(1,11):
            print("Artist " + str(y) + ": " + lt.getElement(datosgenero[1][2],y))
        print("\n")



def printhoras(datoshoras,catalogo,hora_min,hora_max):
    print("\n")
    print("There is a total of " + str(datoshoras[2]) + " reproductions between " + str(hora_min) + " and " + str(hora_max))
    print("======================" + "GENRES SORTED REPRODUCTIONS"  + "======================")
    for y in range(1,10):
        print("TOP " + str(y) + ": " + str(rangoagenero(catalogo,lt.getElement(datoshoras[0], y)[0])) + " with " + str(lt.getElement(datoshoras[0], y)[1]) + " reps.")
    print("The TOP GENRE is " + str(rangoagenero(catalogo,lt.getElement(datoshoras[0], 1)[0])) + " with " + str(lt.getElement(datoshoras[0], 1)[1]) + " reproductions.")
    print("======================" +  " SENTIMENT ANALYSIS" + "======================")
    print(str(rangoagenero(catalogo,lt.getElement(datoshoras[0], 1)[0])) + " has "+ str(lt.size(mp.get(datoshoras[1],lt.getElement(datoshoras[0], 1)[0])["value"]))+ " unique tracks...")
    print("The first TOP 10 tracks are: ")
    for x in range(1,11):
        dato = lt.getElement(datoshoras[3], x)
        print("TOP " + str(x) + " Track: " + str(dato[0]["track_id"]) + " with" + str(lt.size(dato[1])) + "hashtags and VADER = " + str(dato[2]))
    print("\n")
def rangoagenero(catalogo,rango):
    data = catalogo["mapageneros"]
    values = mp.valueSet(data)
    keys = mp.keySet(data)
    for x in range(lt.size(keys)):
        if lt.getElement(values, x) == rango:
             return lt.getElement(keys, x)

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
        listando = True
        listabusqueda = lt.newList("ARRAY_LIST")
        while listando:
            genero = input("Ingrese un género que quiere buscar, si quiere parar de ingresar géneros deje vacío el espacio: ")
            if genero != "":
                lt.addLast(listabusqueda,genero)
            else:
                listando = False
        tracksgeneros  = tracksgeneros(catalogo,listabusqueda)
        printgeneros(tracksgeneros,catalogo)

    elif int(inputs[0]) == 6:
        hora_min = input("Indique la hora y los minutos mínima en hora militar (ej: 13:00): ")
        hora_max = input("Indique la hora y los minutos máximos en hora militar (ej: 13:00): ")
        datoshoras = datoshoras(catalogo,hora_min,hora_max)
        printhoras(datoshoras,catalogo,hora_min,hora_max)
    else:
        sys.exit(0)
sys.exit(0)
