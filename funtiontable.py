#! /usr/bin/emv python
# -*- coding: utf-8 -*-

import re

def tabla(data, lineas):
  data=data
  lineas = lineas
  color=escalar=rotar=trasladar=dibujar=''
  c={}
  for a in lineas:
    palabras = a.split(' ')
    id=tipo=' '
    for b in palabras:
      if re.findall('[a-z]+[\d]+', b):
        id=b
      if re.findall('((Punto)|(Recta)|(Parabola)|(Hiperbola)|(SemiRecta)|(Segmento)|(Curva)|(Circunferencia)|(Cuadrilatero)|(Triangulo)|(Cono)|(Esfera)|(Elipse)|(Cilindro))', b):
        tipo=b
        c[id]=tipo
      if re.findall('Rotar', b):
        rotar+=a+'\n'
      if re.findall('Escalar', b):
        escalar+=a+'\n'
      if re.findall('Colorear', b):
        color+=a+'\n'
      if re.findall('Trasladar', b):
        trasladar+=a+'\n'
      if re.findall('Dibujar', b):
        dibujar += a+'\n'
  return c, rotar, escalar, color, trasladar, dibujar
  
def rotar(lineas):
  lineas=lineas
  r={}
  for a in lineas:
    palabras = a.split(' ')
    id=v=' '
    for b in palabras:
      if re.findall('[a-z]+[\d]+', b):
        id=b
      if re.findall('[\-]?[0-9]{1,}(\.[0-9]{1,})?', b):
        v=b
        r[id]=v
        
  return r

def escalar(lineas):
  lineas=lineas
  e={}
  for a in lineas:
    palabras = a.split(' ')
    id=v=' '
    for b in palabras:
      if re.findall('[a-z]+[\d]+', b):
        id=b
      if re.findall('[\-]?[0-9]{1,}(\.[0-9]{1,})?', b):
        v=b
        e[id]=v
        
  return e
  
def color(lineas):
  lineas=lineas
  c={}
  for a in lineas:
    palabras = a.split(' ')
    id=color=' '
    for b in palabras:
      if re.findall('[a-z]+[\d]+', b):
        id=b
      if re.findall('([rR]ojo)|([aA]zul)|([aA]marillo)|([vV]erde)|([mM]orado)|([gG]ris)|([nN]egro)|([rR]osado)', b):
        color=b
        c[id]=color
        print c
        
  return c
  
def trasladar(lineas):
  lineas=lineas
  t_x={}
  t_y={}
  for a in lineas:
    palabras = a.split(' ')
    x=id=v=' '
    for b in palabras:
      if re.findall('(x)|(y)', b):
        x=b
      if re.findall('[a-z]+[\d]+', b):
        id=b
      if re.findall('[\-]?[0-9]{1,}(\.[0-9]{1,})?', b):
        v=b
        if x=='x':
          t_x[id]=v
        if x=='y':
          t_y[id]=v
        
  return t_x, t_y
  
def dibujar(lineas):
  lineas=lineas
  d={}

  for a in lineas:
    palabras = a.split(' ')
    id=' '
    v=int(0)
    for b in palabras:
      if re.findall('Dibujar', b):
        v=1
        print v
      if re.findall('[a-z]+[\d]+', b):
        id=b
        d[id]=v
  return d

def coord(lineas):
  lineas=lineas
  X={}
  
  Y={}
  for a in lineas:
    palabras = a.split(' ')
    id=x=v=' '
    for b in palabras:
      if re.findall('(x)|(y)', b):
        x=b
      if re.findall('[a-z]+[\d]+', b):
        id=b
      if re.findall('[\-]?[0-9]{1,}(\.[0-9]{1,})?', b):
        v=b
        if x=='x':
          X[id]=v
        if x=='y':
          Y[id]=v
  return X, Y

def extremo(lineas):
  lineas=lineas
  A={}
  B={}
  
  for a in lineas:
    palabras = a.split(' ')
    id=x=v=' '
    for b in palabras:
      if re.findall('(A)|(B)', b):
        x=b
      if re.findall('[a-z]+[\d]+', b):
        id=b
      if re.findall('[\-]?[0-9]{1,}(\.[0-9]{1,})?', b):
        v=b
        if x=='A':
          A[id]=v
        if x=='B':
          B[id]=v
  return A, B

def circulo(lineas):
  lineas=lineas
  r={}
  c={}
  
  for a in lineas:
    palabras = a.split(' ')
    id=x=v=' '
    i=p=0
    for b in palabras:
      if re.findall('(centro)|(radio)', b):
        x=b
      if p==0:
        if re.findall('[a-z]+[\d]+', b):
          id=b
          p=1
      if i==2:
        if x=='centro':
          if re.findall('[a-z]+[\d]+', b):
            v=b
            c[id]=v
        elif x=='radio':
          if re.findall('[\-]?[0-9]{1,}(\.[0-9]{1,})?', b):
            v=b
            r[id]=v
      if re.findall('asignar', b):
        i=2
  return c, r

def vertice(lineas):
  lineas=lineas
  A={}
  B={}
  C={}
  
  for a in lineas:
    palabras = a.split(' ')
    id=x=v=' '
    i=p=0
    for b in palabras:
      if re.findall('(A)|(B)|(C)', b):
        x=b
      if p==0:
        if re.findall('[a-z]+[\d]+', b):
          id=b
          p=1
      if i==2:
        if re.findall('[a-z]+[\d]+', b):
          v=b
          if x=='A':
            A[id]=v
          if x=='B':
            B[id]=v
          if x=='C':
            C[id]=v
      if re.findall('asignar', b):
        i=2
  return A, B, C

def cuadrado(lineas):
  lineas=lineas
  A={}
  B={}
  C={}
  D={}
  
  for a in lineas:
    palabras = a.split(' ')
    id=x=v=' '
    i=p=0
    for b in palabras:
      if re.findall('(A)|(B)|(C)|(D)', b):
        x=b
      if re.findall('[a-z]+[\d]+', b) and p==0:
        id=b
        p=1
      if re.findall('[a-z]+[\d]+', b) and i==2:
        v=b
        if x=='A':
          A[id]=v
        if x=='B':
          B[id]=v
        if x=='C':
          C[id]=v
        if x=='D':
          D[id]=v
      if re.findall('asignar', b):
        i=2

  return A, B, C, D

def semieje(lineas):
  lineas=lineas
  A={}
  B={}
  C={}
  
  for a in lineas:
    palabras = a.split(' ')
    id=x=x1=v=' '
    i=p=0
    for b in palabras:
      if re.findall('(centro)|(semiEje)', b):
        x=b
      if re.findall('[a-z]+[\d]+', b) and p==0:
        id=b
        p=1
      if re.findall('[a-z]+[\d]+', b) and i==2:
        v=b
        C[id]=v
      if re.findall('(A)|(B)', b):
        x1=b
        print x1
      if re.findall('[\-]?[0-9]{1,}(\.[0-9]{1,})?', b):
        v=b
        if x1=='A':
          A[id]=v
        if x1=='B':
          B[id]=v
      if re.findall('asignar', b):
        i=2

  return A, B, C

def atributos(lineas, tipos):
  lineas=lineas
  tipos=tipos
  lcoordenada=lextremo=lvertice=lsemiEje=lcirculo=lcuadrado=lhiper=' '
  Coordenada={}
  Extremo={}
  Vertice={}
  Elipse={}
  Circulo={}
  Cuadrado={}
  Hiperbola={ }

  for key in tipos.keys():
    for b in lineas:
      if tipos[key]=='Punto':
        if re.findall('coordenada', b):
          lcoordenada+=b+'\n'
      if tipos[key]=='Recta':
        if re.findall('extremo', b):
          lextremo+=b+'\n'
      if tipos[key]=='Triangulo':
        if re.findall('vertice', b):
          lvertice+=b+'\n'
      if tipos[key]=='Elipse':
        if re.findall('(centro)|(semiEje)', b):
          lsemiEje+=b+'\n'
      if tipos[key]=='Circunferencia':
        if re.findall('(centro)|(radio)', b):
          lcirculo+=b+'\n'
      if tipos[key]=='Cuadrilatero':
        if re.findall('vertice', b):
          lcuadrado+=b+'\n'
      if tipos[key]=='Hiperbola':
        if re.findall('(centro)|(semiEje)', b):
          lhiper+=b+'\n'

  lcoordenada = lcoordenada.splitlines()
  Coordenada = coord(lcoordenada)
  lextremo = lextremo.splitlines()
  Extremo = extremo(lextremo)
  print lvertice
  lvertice = lvertice.splitlines()
  Vertice = vertice(lvertice)
  lsemiEje = lsemiEje.splitlines()
  Elipse = semieje(lsemiEje)
  lcirculo = lcirculo.splitlines()
  Circulo = circulo(lcirculo)
  lcuadrado = lcuadrado.splitlines()
  Cuadrado = cuadrado(lcuadrado)
  lhiper = lhiper.splitlines()
  Hiperbola = semieje(lhiper)

  return Coordenada, Extremo, Vertice, Elipse, Circulo, Cuadrado, Hiperbola

def simbolos(data, lineas):
  data=data
  lineas=lineas

  identificadores = tabla(data, lineas)
  lrotar = identificadores[1].splitlines()
  lescalar = identificadores[2].splitlines()
  lcolor = identificadores[3].splitlines()
  ltrasladar = identificadores[4].splitlines()
  ldibujar = identificadores[5].splitlines()
  Rotar = rotar(lrotar)
  Escalar = escalar(lescalar)
  Trasladar = trasladar(ltrasladar)
  Color = color(lcolor)
  Dibujar = dibujar(ldibujar)
  Atributos = atributos(lineas, identificadores[0])
  
  keys = identificadores[0]
  simbolos=[]
  for i in range(len(keys)):
    simbolos.append([])
    simbolos[i].append(i)

  i=0
  for key in keys.keys():
    simbolos[i].append(key)
    simbolos [i].append(keys[key])
    if keys[key]=='Punto':
      coord = Atributos[0]
      simbolos[i].append(coord[0][key])
      simbolos[i].append(coord[1][key])
    if keys[key]=='Recta':
      sec = Atributos[1]
      simbolos[i].append(sec[0][key])
      simbolos[i].append(sec[1][key])
    if keys[key]=='Triangulo':
      vert = Atributos[2]
      simbolos[i].append(vert[0][key])
      simbolos[i].append(vert[1][key])
      simbolos[i].append(vert[2][key])
    if keys[key]=='Elipse':
      elip = Atributos[3]
      simbolos[i].append(elip[0][key])
      simbolos[i].append(elip[1][key])
      simbolos[i].append(elip[2][key])
    if keys[key]=='Circunferencia':
      cir = Atributos[4]
      simbolos[i].append(cir[0][key])
      simbolos[i].append(cir[1][key])
    if keys[key]=='Cuadrilatero':
      cuad = Atributos[5]
      simbolos[i].append(cuad[0][key])
      simbolos[i].append(cuad[1][key])
      simbolos[i].append(cuad[2][key])
      simbolos[i].append(cuad[3][key])
    if keys[key]=='Hiperbola':
      hipe = Atributos[6]
      simbolos[i].append(hipe[2][key])
      simbolos[i].append(hipe[0][key])
      simbolos[i].append(hipe[1][key])
    if Rotar.has_key(key)==True:
      simbolos[i].append(Rotar[key])
    else:
      simbolos[i].append(0)
    if Escalar.has_key(key)==True:
      simbolos[i].append(Escalar[key])
    else:
      simbolos[i].append(0)
    if Trasladar[0].has_key(key)==True:
      simbolos[i].append(Trasladar[0][key])
    else:
      simbolos[i].append(0)
    if Trasladar[1].has_key(key)==True:
      simbolos[i].append(Trasladar[1][key])
    else:
      simbolos[i].append(0)
    if Color.has_key(key)==True:
      simbolos[i].append(Color[key])
    else:
      simbolos[i].append(0)
    if Dibujar.has_key(key)==True:
      simbolos[i].append(Dibujar[key])
    else:
      simbolos[i].append(0)
    i=i+1

    """
    Se genera una tabla  con los siguientes datos y en la posicion que sigue:
    Posición Identificador Tipo A B C D Rotar Escalar Trasladar X Trasladar Y Color
    para el punto A=X, B=y
    para la circunferencia centro = A, radio=B
    para la elipse y la hiperbola centro=A, semiEje A=B, semiEje=C
    """
  return simbolos
