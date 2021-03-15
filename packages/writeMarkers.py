# -*- coding: utf-8 -*-
import json
import sys
import time
import os

def writeMarker():
    markers = json.loads(open('databases/markersDB.json').read())
    print (markers)
    marker = input('Ingrese el nombre para el marcador: \n')
    url = input('Ingrese la direccion web: \n')
    comment = input('Comentarios sobre la web o acceso: \n')
    user = input('Ingrese el usuario de acceso: \n')
    password = input('Ingrese la contraseña:')
    op = {"url": url, "comment": comment, "access": {"user": user, "pass": password}}
    markers["markers"][marker] = op
    print (markers)
    markersDump = open('databases/markersDB.json', 'w')
    markersDump.write(json.dumps(markers, indent=4))
    markersDump.close()
    #print (markers)
