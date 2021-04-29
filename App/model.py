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
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""


def crear_catalogo():
    catalogo = {"datosusuarios": om.newMap(),
                "datoscanciones": om.newMap(),
                "datossentimientos": om.newMap()}
    return catalogo

def addinstance(catalogo, x):
    if not om.contains(catalogo["datosusuarios"], str(x["user_id"])+  str(x["track_id"]) + str(x["created_at"]) ):
        om.put(catalogo["datosusuarios"], str(x["user_id"])+  str(x["track_id"]) + str(x["created_at"]), x)
    else:
        dato = om.get(catalogo["datosusuarios"], str(x["user_id"])+  str(x["track_id"]) + str(x["created_at"]))["value"]["hashtag"]
        dato = dato + "," + x["hashtag"]

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