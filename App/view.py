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
    
    elif int(inputs[0]) == 4:
        mininstrum=float(input("Ingrese el valor minimo deseado del rango para Instrumentalness: "))
        maxinstrum=float(input("Ingrese el valor maximo deseado del rango para Instrumentalness: "))
        mintempo=float(input("Ingrese el valor minimo deseado del rango para el tempo: "))
        maxtempo=float(input("Ingrese el valor maximo deseado del rango para el tempo: "))
    
    elif int(inputs[0]) == 5:
        pass

    elif int(inputs[0]) == 6:
        pass
    else:
        sys.exit(0)
sys.exit(0)
