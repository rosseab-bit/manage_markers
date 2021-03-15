# -*- coding: utf-8 -*-
import os
import sys
import time
import json
from os import listdir
def loadJson():
    markers = '../databases/markersDB.json'
    path_db = '.'
    json_template = {'markers':{}}
    print (os.listdir(path_db))
    if "markersDB.json" not in os.listdir(path_db):
        print (path_db)
        print ("----- Buscando en base de datos ------")
        time.sleep(2)
        print ('La base de datos no fue creada')
        print ('Desea crear la base de datos ? yes/no: ')
        option = input()
        if option == "yes":
            print ('----- Creando base de datos -----')
            os.system('> ../databases/markersDB.json')
            time.sleep(2)
            dataDump = open('../databases/markersDB.json', 'w')
            dataDump.write(json.dumps(json_template, indent=4))
            dataDump.close()
        else:
            print ("--------------------------------------")
            return print ('Para que el programa funcione correctamente \n es necesario crear una base de datos.')
loadJson()
