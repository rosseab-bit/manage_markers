# -*- coding: utf-8 -*-
import json
import sys
import time
import os

def dellMarker():
    markers = json.loads(open('databases/markersDB.json').read())
    n = 0
    listMark = []
    for mark in markers["markers"]:
        print(str(n)+": "+mark)
        listMark.append(mark)
        n = n+1
    option = input('Desea eliminar algun marcador? yes/no: \n')
    if option == "yes":
        dellMark = input('Escriba el nombre del marcador que desea eliminar: \n')
        for mark in markers:
            del markers["markers"][dellMark]
        print ("Se elimino el marcador: "+mark)
    markersDump = open('databases/markersDB.json', 'w')
    markersDump.write(json.dumps(markers, indent=4))
    markersDump.close()
