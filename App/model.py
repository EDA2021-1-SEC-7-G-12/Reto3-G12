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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.DataStructures import rbt
from DISClib.Algorithms.Sorting import mergesort as ms 
import random as rd
assert cf


"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""


def crear_catalogo():
    catalogo = {"datosusuarios": om.newMap(),
                "datoscanciones": om.newMap(),
                "datossentimientos": om.newMap(),
                "mapageneros": mp.newMap(20, maptype="PROBING")}
    return catalogo

def addinstance(catalogo, x):
    if not om.contains(catalogo["datosusuarios"], str(x["user_id"])+  str(x["track_id"]) + str(x["created_at"]) ):
        om.put(catalogo["datosusuarios"], str(x["user_id"])+  str(x["track_id"]) + str(x["created_at"]), x)
    else:
        dato = om.get(catalogo["datosusuarios"], str(x["user_id"])+  str(x["track_id"]) + str(x["created_at"]))["value"]["hashtag"]
        dato = dato + "," + x["hashtag"]

def loadgeneros(catalogo):
    mp.put(catalogo["mapageneros"],"Reggae", (60,90))
    mp.put(catalogo["mapageneros"],"Down-tempo", (70,100))
    mp.put(catalogo["mapageneros"],"Chill-out", (90,120))
    mp.put(catalogo["mapageneros"],"Hip-hop", (85,115))
    mp.put(catalogo["mapageneros"],"Jazz and Funk ", (120,125))
    mp.put(catalogo["mapageneros"],"Pop", (100,130))
    mp.put(catalogo["mapageneros"],"R&B", (60,80))
    mp.put(catalogo["mapageneros"],"Rock", (110,140))
    mp.put(catalogo["mapageneros"],"Metal", (100,160))


def addsong(catalogo, x):
    om.put(catalogo["datoscanciones"], str(x["user_id"]) + str(x["track_id"]) + str(x["created_at"]), x)

def addfeel(catalogo, x):
    om.put(catalogo["datossentimientos"], str(x["hashtag"]), x)

def numerocaracteristicasrango(catalogo,cont,minimo,maximo):
    numerotracks = 0
    numeroartistas = 0
    listartista = lt.newList("ARRAY_LIST")
    datos = rbt.valueSet(catalogo["datoscanciones"])
    for y in range(datos["size"]):
        x = lt.getElement(datos,y)
        if (float(x[cont]) >= minimo) and (float(x[cont]) <= maximo):
            if om.contains(catalogo["datosusuarios"], str(x["user_id"]) + str(x["track_id"]) + str(x["created_at"])):
                numerotracks += 1
                if not lt.isPresent(listartista, x["artist_id"]):
                    lt.addLast(listartista, x["artist_id"])
                    numeroartistas += 1
    return numerotracks, numeroartistas

def numerocaracteristicasrango2(catalogo,cont,minimo,maximo):
    numerotracks = 0
    numeroartistas = 0
    listartista = lt.newList("ARRAY_LIST")
    datos = rbt.valueSet(catalogo["datoscanciones"])
    for y in range(datos["size"]):
        x = lt.getElement(datos,y)
        if (float(x[cont]) >= minimo) and (float(x[cont]) <= maximo):
            if om.contains(catalogo["datosusuarios"], str(x["user_id"]) + str(x["track_id"]) + str(x["created_at"])):
                numerotracks += 1
                if not lt.isPresent(listartista, x["artist_id"]):
                    lt.addLast(listartista, x["artist_id"])
                    numeroartistas += 1
    numero = rd.randint(1,lt.size(listartista)-10)
    randomartists = lt.subList(listartista,numero,10)
    return numerotracks, numeroartistas, randomartists

def numerotracksenergydance(catalogo,minenergy,maxenergy,mindance,maxdance):
    numerotracks = 0
    listracks = lt.newList("ARRAY_LIST")
    data = om.valueSet(catalogo["datoscanciones"])
    trackmap = mp.newMap(1000000, maptype="PROBING")
    for x in range(data["size"]):
        y = lt.getElement(data, x)
        if not mp.contains(trackmap, y["track_id"]):
            if (minenergy <= float(y["energy"]) <= maxenergy) and (mindance <= float(y["danceability"]) <= maxdance):
                lt.addLast(listracks, y)
                numerotracks += 1
                mp.put(trackmap, y["track_id"], None)
    return numerotracks, listracks

def numerotracksestudiar(catalogo, mininstrum, maxinstrum, mintempo, maxtempo):
    numerotracks = 0
    listracks = lt.newList("ARRAY_LIST")
    data = om.valueSet(catalogo["datoscanciones"])
    trackmap = mp.newMap(1000000, maptype="PROBING")
    for x in range(data["size"]):
        y = lt.getElement(data, x)
        if not mp.contains(trackmap, y["track_id"]):
            if (mininstrum <= float(y["instrumentalness"]) <= maxinstrum) and (mintempo <= float(y["tempo"]) <= maxtempo):
                lt.addLast(listracks, y)
                numerotracks += 1
                mp.put(trackmap, y["track_id"], None)
    return numerotracks, listracks

def tracksgeneros(catalogo,listabusqueda):
    nuevalistabusqueda = lt.newList("ARRAY_LIST")
    for x in range(lt.size(listabusqueda)):
        genero = lt.getElement(listabusqueda,x)
        if not mp.contains(catalogo["mapageneros"],genero):
            respuesta = input("El género " + genero + " no está en la lista de géneros, desea añadirlo? (y/n): ")
            if respuesta == "y":
                minimo = float(input("Ingrese el tempo mínimo: "))
                maximo = float(input("Ingrese el tempo máximo: "))
                mp.put(catalogo["mapageneros"],genero,(minimo,maximo))
                print("Género añadido.")
                lt.addLast(nuevalistabusqueda,genero)
        else:
            lt.addLast(nuevalistabusqueda,genero)
    # Creamos otra lista de busqueda para excluir en la búsqueda los géneros no deseados.
    listaresultados = lt.newList("ARRAY_LIST")
    numerototal = om.size(catalogo["datoscanciones"])
    lt.addLast(listaresultados,numerototal)
    for x in range(lt.size(nuevalistabusqueda)):
        genero = lt.getElement(nuevalistabusqueda,x)
        lt.addLast(listaresultados,(genero,numerocaracteristicasrango2(catalogo,"tempo",mp.get(catalogo["mapageneros"],genero)["value"][0],mp.get(catalogo["mapageneros"],genero)["value"][1])))
    return listaresultados

def datoshoras(catalogo,hora_min,hora_max):
    generos = mp.keySet(catalogo["mapageneros"])
    songs = catalogo["datoscanciones"]
    datakeys = om.keySet(songs)
    songsgeneros = mp.newMap(20, maptype="PROBING")
    for x in range(lt.size(generos)):
        genero = lt.getElement(generos, x)
        mp.put(songsgeneros,mp.get(catalogo["mapageneros"],genero)["value"],lt.newList("ARRAY_LIST"))
    numrep = 0
    listageneros = mp.keySet(songsgeneros)
    for x in range(datakeys["size"]):
        key = lt.getElement(datakeys, x)
        if  (int(key[-8]+key[-7]) >= int(hora_min.split(":")[0])) and (int(key[-5]+key[-4]) >= int(hora_min.split(":")[1])) and (int(key[-8]+key[-7]) <= int(hora_max.split(":")[0])) and (int(key[-5]+key[-4]) <= int(hora_max.split(":")[1])):
            generosong = checkgeneros(om.get(songs,key)["value"], listageneros)
            for y in range(lt.size(generosong)):
                llavegenero = lt.getElement(generosong, y)
                lt.addLast(mp.get(songsgeneros,(llavegenero))["value"],om.get(songs,key)["value"])
            numrep += 1
    generosrep = lt.newList("ARRAY_LIST")
    for x in range(lt.size(listageneros)):
        generooo = lt.getElement(listageneros,x)
        lt.addLast(generosrep,(generooo ,lt.size(mp.get(songsgeneros,generooo)["value"])))
    generosorteados = ms.sort(generosrep, compgeneros)
    generomax = lt.getElement(generosorteados, 1)[0]
    listamax = mp.get(songsgeneros,generomax)["value"]
    listapasortearhashtags = lt.newList("ARRAY_LIST")
    dataa = om.valueSet(catalogo["datosusuarios"])
    maptags = mp.newMap(100000, maptype="PROBING")
    for x in range(lt.size(dataa)):
        listen = lt.getElement(dataa,x)
        created = listen["created_at"]
        if  (int(created[-8]+created[-7]) >= int(hora_min.split(":")[0])) and (int(created[-5]+created[-4]) >= int(hora_min.split(":")[1])) and (int(created[-8]+created[-7]) <= int(hora_max.split(":")[0])) and (int(created[-5]+created[-4]) <= int(hora_max.split(":")[1])):
            if mp.contains(maptags, listen["track_id"]):
                if not lt.isPresent(mp.get(maptags, listen["track_id"])["value"], listen["hashtag"]):
                    lt.addLast(mp.get(maptags, listen["track_id"])["value"], listen["hashtag"])
            else:
                mp.put(maptags,listen["track_id"],lt.newList("ARRAY_LIST"))
            lt.addLast(mp.get(maptags, listen["track_id"])["value"], listen["hashtag"])
    listaidsusados = lt.newList("ARRAY_LIST")
    for x in range(lt.size(listamax)):
        song = lt.getElement(listamax, x)
        if not lt.isPresent(listaidsusados,song["track_id"]):
            lt.addLast(listapasortearhashtags, (song,vaderprom(catalogo, mp.get(maptags,song["track_id"])["value"])[1],vaderprom(catalogo, mp.get(maptags,song["track_id"])["value"])[0]))
            lt.addLast(listaidsusados,song["track_id"])
    songhashsort = ms.sort(listapasortearhashtags, compgeneros)
    lista10 = lt.subList(songhashsort, 1, 10)
    return generosorteados,songsgeneros,numrep, lista10 





def compgeneros(g1,g2):
    return g1[1] > g2[1]

def checkgeneros(cancion,listageneros):
    listageneros2 = lt.newList("ARRAY_LIST")
    for x in range(listageneros["size"]):
        rango = lt.getElement(listageneros,x)
        if (float(cancion["tempo"]) <= rango[1]) and (float(cancion["tempo"]) >= rango[0]):
            lt.addLast(listageneros2, rango)
    return listageneros2


def comphashtags(h1,h2):
    return lt.size(h1[1]) > lt.size(h2[1])

def vaderprom(catalogo,hashtags):
    tagsusados = lt.newList("ARRAY_LIST")
    vaders = 0
    totalvaders = 0
    data = catalogo["datossentimientos"]
    for x in range(lt.size(hashtags)):
        tag = lt.getElement(hashtags, x).lower()
        if not lt.isPresent(tagsusados,tag):
            if(om.contains(data,tag)):
                dato = om.get(data,tag)["value"]
                if dato["vader_avg"] != "":
                    vaders += 1
                    totalvaders += float(dato["vader_avg"])
            lt.addLast(tagsusados,tag)
    if not vaders == 0:
        return round(totalvaders/vaders,1),lt.size(tagsusados)
    else:
        return None,lt.size(tagsusados)

