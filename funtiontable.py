#! /usr/bin/emv python
# -*- coding: utf-8 -*-

import re

#extrae los identificadores y los Tipos, tambien las lineas de rotar, escalar, trasladar y dibujar
def tabla(data, lineas):
  data=data
  lineas = lineas
  color=escalar=rotar=trasladar=dibujar=''
  c={}
  for a in lineas:
    palabras = a.split(' ')
    id=tipo=' '
    i=0
    for b in palabras:
      if re.findall('#', b):
        i=1
      if i==0:
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
  
#función que extrae el identificador y el valor a rotar
def rotar(lineas):
  lineas=lineas
  r={}
  for a in lineas:
    palabras = a.split(' ')
    id=v=' '
    i=0
    for b in palabras:
      if re.findall('[a-z]+[\d]+', b):
        id=b
      if re.findall('[\-]?[0-9]{1,}(\.[0-9]{1,})?', b):
        v=b
        r[id]=v
        
  return r

#función que extrae el identificador y e valor deescalar 
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
  
#función que extrae el identificador y su color
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
  
#función que extrae el identificador y e valor trasladar (x, y)
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
  
#función que extrae el identificador y si se va a dibujar
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

#funciones de los valores del punto
def coord(lineas):
  lineas=lineas
  X={}
  
  Y={}
  for a in lineas:
    palabras = a.split(' ')
    id=x=v=' '
    i=0
    for b in palabras:
      if re.findall('#', b):
        i=1
      if i==0:
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

#funciones de los valores de la recta
def extremo(lineas):
  lineas=lineas
  A={}
  B={}
  
  for a in lineas:
    palabras = a.split(' ')
    id=x=v=' '
    p=i=t=0
    for b in palabras:
      if re.findall('#', b):
        t=1
      if t==0:
        if re.findall('(A)|(B)', b):
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
        if re.findall('asignar', b):
          i=2
  return A, B

def circulo(lineas):
  lineas=lineas
  r={}
  c={}
  
  for a in lineas:
    palabras = a.split(' ')
    id=x=v=' '
    i=p=t=0
    for b in palabras:
      if re.findall('#', b):
        t=1
      if t==0:
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
  return r, c

#funciones de los valores del triangulo
def vertice(lineas):
  lineas=lineas
  A={}
  B={}
  C={}
  
  for a in lineas:
    palabras = a.split(' ')
    id=x=v=' '
    i=p=t=0
    for b in palabras:
      if re.findall('#', b):
        t=1
      if re.findall('(A)|(B)|(C)', b) and t==0:
        x=b
      if p==0 and t==0:
        if re.findall('[a-z]+[\d]+', b):
          id=b
          p=1
      if i==2 and t==0:
        if re.findall('[a-z]+[\d]+', b):
          v=b
          if x=='A':
            A[id]=v
          if x=='B':
            B[id]=v
          if x=='C':
            C[id]=v
      if re.findall('asignar', b) and t==0:
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
    i=p=t=0
    for b in palabras:
      if re.findall('#', b):
        t=1
      if re.findall('(A)|(B)|(C)|(D)', b) and t==0:
        x=b
      if re.findall('[a-z]+[\d]+', b) and p==0 and t==0:
        id=b
        p=1
      if re.findall('[a-z]+[\d]+', b) and i==2 and t==0:
        v=b
        if x=='A':
          A[id]=v
        if x=='B':
          B[id]=v
        if x=='C':
          C[id]=v
        if x=='D':
          D[id]=v
      if re.findall('asignar', b) and t==0:
        i=2

  return A, B, C, D

#funciones de los valores de la elipse y la hiperbola
def semieje(lineas):
  lineas=lineas
  A={}
  B={}
  C={}
  
  for a in lineas:
    palabras = a.split(' ')
    id=x=x1=v=' '
    i=p=t=0
    for b in palabras:
      if re.findall('#', b):
        t=1
      if re.findall('(centro)|(semiEje)', b) and t==0:
        x=b
      if re.findall('[a-z]+[\d]+', b) and p==0 and t==0:
        id=b
        p=1
      if re.findall('[a-z]+[\d]+', b) and i==2 and t==0:
        v=b
        C[id]=v
      if re.findall('(A)|(B)', b):
        x1=b
        print x1
      if re.findall('[\-]?[0-9]{1,}(\.[0-9]{1,})?', b) and t==0:
        v=b
        if x1=='A':
          A[id]=v
        if x1=='B':
          B[id]=v
      if re.findall('asignar', b) and t==0:
        i=2

  return A, B, C

#función de los valores de la parabola
def parabola(lineas):
  lineas=lineas
  o={}
  e={}
  
  for a in lineas:
    palabras = a.split(' ')
    id=x=v=' '
    i=p=t=0
    for b in palabras:
      if re.findall('#', b):
        t=1
      if re.findall('(origen)|(escala)', b) and t==0:
        x=b
      if p==0 and t==0:
        if re.findall('[a-z]+[\d]+', b):
          id=b
          p=1
      if i==2 and t==0:
        if x=='origen':
          if re.findall('[a-z]+[\d]+', b):
            v=b
            o[id]=v
        elif x=='escala':
          if re.findall('[\-]?[0-9]{1,}(\.[0-9]{1,})?', b) and t==0:
            v=b
            e[id]=v
      if re.findall('asignar', b) and t==0:
        i=2
  return e, o
  
def cono(lineas):
  lineas=lineas
  c_r = circulo(lineas)
  c={}
  
  for a in lineas:
    palabras = a.split(' ')
    id=x=v=' '
    i=p=t=0
    for b in palabras:
      if re.findall('#', b):
        t=1
      if re.findall('altura', b):
        x=b
      if re.findall('[a-z]+[\d]+', b):
        id=b
      if x=='altura' and t==0:
        if re.findall('[\-]?[0-9]{1,}(\.[0-9]{1,})?', b):
          v=b
          c[id]=v

  return c_r[0], c, c_r[1]
  
#función que extrae todos los valores de cada identificador
def atributos(lineas, tipos):
  lineas=lineas
  tipos=tipos
  lcoordenada=lextremo=lvertice=lsemiEje=lcirculo=lcuadrado=lhiper=lparabola=lcono=lesfera=lcilindro=' '
  Coordenada={}
  Extremo={}
  Vertice={}
  Elipse={}
  Circulo={}
  Cuadrado={}
  Hiperbola={ }
  Parabola={}
  Cono={}
  Esfera={}
  Cilindro={}

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
      if tipos[key]=='Parabola':
        if re.findall('(origen)|(escala)', b):
          lparabola+=b+'\n'
      if tipos[key]=='Cono':
        if re.findall('(centro)|(radio)|(altura)', b):
          lcono+=b+'\n'
      if tipos[key]=='Esfera':
        if re.findall('(centro)|(radio)', b):
          lesfera+=b+'\n'
      if tipos[key]=='Cilindro':
        if re.findall('(centro)|(radio)|(altura)', b):
          lcilindro+=b+'\n'

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
  lparabola = lparabola.splitlines()
  Parabola = parabola(lparabola)
  lcono = lcono.splitlines()
  Cono = cono(lcono)
  lesfera = lesfera.splitlines()
  Esfera = circulo(lesfera)
  lcilindro = lcilindro.splitlines()
  Cilindro = cono(lcilindro)

  return Coordenada, Extremo, Vertice, Elipse, Circulo, Cuadrado, Hiperbola, Parabola, Cono, Esfera, Cilindro

#función que devuelve una tabla con todos los identificadores y sus atributos de 2D y 3d
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
      simbolos[i].append(hipe[0][key])
      simbolos[i].append(hipe[1][key])
      simbolos[i].append(hipe[2][key])
    if keys[key]=='Parabola':
      para = Atributos[7]
      simbolos[i].append(para[0][key])
      simbolos[i].append(para[1][key])
    if keys[key]=='Cono':
      cono = Atributos[8]
      simbolos[i].append(cono[0][key])
      simbolos[i].append(cono[1][key])
      simbolos[i].append(cono[2][key])
    if keys[key]=='Esfera':
      esf = Atributos[9]
      simbolos[i].append(esf[0][key])
      simbolos[i].append(esf[1][key])
    if keys[key]=='Cilindro':
      cil = Atributos[10]
      simbolos[i].append(cil[0][key])
      simbolos[i].append(cil[1][key])
      simbolos[i].append(cil[2][key])
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
    Posición Identificador Tipo A B C D Rotar Escalar Trasladar X Trasladar Y Color dibujar
    para el punto A=X, B=y
    para la circunferencia y la esfera radio =A, centro=B
    para la elipse y la hiperbola centro=C, semiEje A=A, semiEje=B
    para la parabola escala=A, centro = B
    para el cono y el cilindro radio=A, altura=B, centro=C
    """
  return simbolos
