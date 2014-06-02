#! /usr/bin/emv python

import tabladesimbolos as funcion

palabras = ' '
archivo = ['ejemplos/cilindro.CG']
tipo=' '
for texto in archivo:
    f = open(texto, 'r')
    data = f.read()
    #palabras = data.split(' )
    lineas = data.splitlines()
    f.close()

#result = funcion.tabla(data, lineas)
#lineas = funcion.atributos(lineas, result[0])
#print lineas
h = funcion.simbolos(data, lineas)
n = len(h)
for i in h[0]:
  print i
