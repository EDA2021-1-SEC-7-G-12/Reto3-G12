"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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

import time
import tracemalloc
import config as cf
import model
import csv

def crear_catalogo():
    return model.crear_catalogo()

def loaddatos(catalogo):
    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()

    loaduser(catalogo)
    loadmusic(catalogo)
    loadfeelings(catalogo)
    loadgeneros(catalogo)

    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)
    return delta_memory,delta_time


def loadgeneros(catalogo):
    model.loadgeneros(catalogo)

def loaduser(catalogo):
    userfile = cf.data_dir  + "user_track_hashtag_timestamp-small.csv"
    input_file = csv.DictReader(open(userfile, encoding='utf-8'))
    for x in input_file:
        model.addinstance(catalogo, x)

def loadmusic(catalogo):
    musicfile = cf.data_dir + "context_content_features-small.csv"
    input_file = csv.DictReader(open(musicfile, encoding='utf-8'))
    for x in input_file:
        model.addsong(catalogo, x)

def loadfeelings(catalogo):
    feelsfile = cf.data_dir + "sentiment_values.csv"
    input_file = csv.DictReader(open(feelsfile, encoding='utf-8'))
    for x in input_file:

        model.addfeel(catalogo, x)

def numerocaracteristicasrango(catalogo,cont,minimo,maximo):
    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()

    result = model.numerocaracteristicasrango(catalogo,cont,minimo,maximo)

    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)
    return result,delta_memory,delta_time
    

def numerotracksenergydance(catalogo,minenergy,maxenergy,mindance,maxdance):
    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()

    result = model.numerotracksenergydance(catalogo,minenergy,maxenergy,mindance,maxdance)
    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)
    return result,delta_memory,delta_time
    

def numerotracksestudiar(catalogo, mininstrum, maxinstrum, mintempo, maxtempo):
    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()

    result = model.numerotracksestudiar(catalogo, mininstrum, maxinstrum, mintempo, maxtempo)
    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)
    return result,delta_memory,delta_time
    

def tracksgeneros(catalogo,listabusqueda):
    return model.tracksgeneros(catalogo,listabusqueda)
    

def datoshoras(catalogo,hora_min,hora_max):
    return model.datoshoras(catalogo,hora_min,hora_max)
    
def getTime():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """

    return float(time.perf_counter()*1000)


def getMemory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def deltaMemory(start_memory, stop_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory