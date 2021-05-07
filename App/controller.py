﻿"""
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

import config as cf
import model
import csv

def crear_catalogo():
    return model.crear_catalogo()

def loaddatos(catalogo):
    loaduser(catalogo)
    loadmusic(catalogo)
    loadfeelings(catalogo)
    loadgeneros(catalogo)

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
    return model.numerocaracteristicasrango(catalogo,cont,minimo,maximo)

def numerotracksenergydance(catalogo,minenergy,maxenergy,mindance,maxdance):
    return model.numerotracksenergydance(catalogo,minenergy,maxenergy,mindance,maxdance)

def numerotracksestudiar(catalogo, mininstrum, maxinstrum, mintempo, maxtempo):
    return model.numerotracksestudiar(catalogo, mininstrum, maxinstrum, mintempo, maxtempo)

def tracksgeneros(catalogo,listabusqueda):
    return model.tracksgeneros(catalogo,listabusqueda)