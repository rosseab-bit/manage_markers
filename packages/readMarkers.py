# -*- coding: utf-8 -*- 
import json
import sys
import os
import time

def readMarkers():
    markersDB = 'databases/markersDB.json'
    markers = json.loads(open(markersDB).read())
    mark_list = []
    n = 0
    if len(markers["markers"]) < 1:
        print ("----- Buscando en base de datos ------")
        time.sleep(2)
        return print ("Todavia no ingresaste ningun marcador")
    for mark in markers["markers"]:
        mark_list.append(mark)
        print (str(n)+": "+mark)
        n = n+1
    print ("Ingerse el numero del marcador: ")
    mark_num = input()
    print ("----- Buscando en base de datos ------")
    time.sleep(2)
    print ("# Acceso a " + mark_list[int(mark_num)])
    print ("Comment: " + markers["markers"][mark_list[int(mark_num)]]["comment"])
    print ("url: " + markers["markers"][mark_list[int(mark_num)]]["url"])
    print ("user: " + markers["markers"][mark_list[int(mark_num)]]["access"]["user"])
    print ("pass: " + markers["markers"][mark_list[int(mark_num)]]["access"]["pass"])

