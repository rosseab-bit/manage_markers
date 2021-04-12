# -*- coding: utf-8 -*- 
import json
import sys
import os
import time

def editMarkers():
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
    print ("------ Que desea editar ? ------")
    print ("a : comment \nb : url \nc : user \nd : pass")
    print ("Ingrese la letra de del campo que desea editar")
    mark_edit = input()
    if mark_edit == "a":
        option = input("Ingresar comentario:\n")
        markers["markers"][mark_list[int(mark_num)]]["comment"] = option
    elif mark_edit == "b":
        option = input("Ingresar url:\n")
        markers["markers"][mark_list[int(mark_num)]]["url"] = option
    elif mark_edit == "c":
        option = input("Ingresar user:\n")
        markers["markers"][mark_list[int(mark_num)]]["access"]["user"] = option
    elif mark_edit == "d":
        option = input("Ingresar pass:\n")
        markers["markers"][mark_list[int(mark_num)]]["access"]["pass"] = option
    else:
        print ("------ Dese seguir editando ? yes/no:  ------\n")
        option = input()
        if option == "yes":
            print ()
            print ("a : comment \nb : url \nc : user \nd : pass")
            print ("Ingrese la letra de del campo que desea editar")
            mark_edit = input()
            if mark_edit == "a":
                option = input("Ingresar comentario:\n")
                markers["markers"][mark_list[int(mark_num)]]["comment"] = option
            elif mark_edit == "b":
                option = input("Ingresar url:\n")
                markers["markers"][mark_list[int(mark_num)]]["url"] = option
            elif mark_edit == "c":
                option = input("Ingresar user:\n")
                markers["markers"][mark_list[int(mark_num)]]["access"]["user"] = option
            elif mark_edit == "d":
                option = input("Ingresar pass:\n")
                markers["markers"][mark_list[int(mark_num)]]["access"]["pass"] = option

        
    

    print ("# Se actualizo el marcador: " + mark_list[int(mark_num)])
    print ("Comment: " + markers["markers"][mark_list[int(mark_num)]]["comment"])
    print ("url: " + markers["markers"][mark_list[int(mark_num)]]["url"])
    print ("user: " + markers["markers"][mark_list[int(mark_num)]]["access"]["user"])
    print ("pass: " + markers["markers"][mark_list[int(mark_num)]]["access"]["pass"])
