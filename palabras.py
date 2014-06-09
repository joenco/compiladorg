#! /usr/bin/emv python

import tabladesimbolos as funcion

palabras = ' '
archivo = ['ejemplos/punto.CG']
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

print "Tabla 1"

for i in h[0]:
  print i

print "Tabla 2"
for i in h[1]:
  print i

