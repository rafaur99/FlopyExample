# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
import numpy as np
import matplotlib.pyplot as plt
import flopy


#parametros inciales del modelo
name = "Ejercicio1_01"
h1 = 100
h2 = 90
Nlay = 10
N = 101
L = 400.0
H = 50.0
k = 1.0

#buscamos la direccion de mf6 y la relacionamos con el trabajo,
#el ejecutable de modflow; aparte se 
#aparte se creo un espacio de trabajo.
sim = flopy.mf6.MFSimulation(
    sim_name=name, exe_name="D:\Semestre 2020-2\CURSO DE DIPLOMADO\mf6.2.0\bin" , version="mf6", 
        sim_ws="workspace"
)   

    #discretizacion del tiempo el mf6
tdis = flopy.mf6.ModflowTdis(
sim, pname="tdis", time_units="DAYS", nper=1, perioddata=[(1.0, 1, 1.0)]
)

#copia de los paquetes de Modflow utilizarlos
ims = flopy.mf6.ModflowIms(sim, pname="ims", complexity="SIMPLE")

# Crea un archivo gwf que es el archivo de flujo
model_nam_file = "{}.nam".format(name)
gwf = flopy.mf6.ModflowGwf(sim, modelname=name, model_nam_file=model_nam_file)   
   
