# -*- coding: utf-8 -*-
import json
import sys
import os
import time
from packages import readMarkers
from packages import writeMarkers
from packages import dellMarkers

def manageMarkers():
    while (True):
        print ("------ Managmen Markers System ------")
        print ("-------------------------------------")
        print ("Elija una de las opciones: ")
        print ("b: buscar \ni: insertar \ne: eliminar")
        option = input('Ingrese la opciones que desea: \n')
        if option == "b":
            print ("------ Accediendo a la base de datos: ------")
            readMarkers.readMarkers()
            print ("------ Exit Database -----")
        elif option == "i":
            print ("------ Accediendo a la base de datos ------")
            writeMarkers.writeMarker()
            print ("------ Ingresando nuevo marcador a la base ------")
            print ("------ Exit Database -----")
        elif option == "e":
            print ("------ Accediendo a la base de datos ------")
            dellMarkers.dellMarker()
            print ("------ Eliminando marcador ------")
            time.sleep(2)
            print ("------ Exit Database -----")
        else:
            print ("------------------------------------------")
            print ("No se reconoce la orden vuelva a intentar.")
        status = input("Desea salir  ? Ingrese: \nsi \nno \n")
        if status == "si":
            break
manageMarkers()
