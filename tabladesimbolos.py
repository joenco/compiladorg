#! /usr/bin/emv python
# -*- coding: utf-8 -*-

import re
import os

#extrae los identificadores y los Tipos, tambien las lineas de rotar, escalar, trasladar y dibujar
def tabla(data, lineas):
  data=data
  lineas = lineas
  lineadibujar=10000
  nlinea=0
  definir=idem=color=escalar=rotar=rotarD=trasladar=dibujar=''
  c={}
  for a in lineas:
    nlinea+=1
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
        if re.findall('(coordenada)|(extremo)|(vertice)|(semiEje)|(potencia)|(origen)|(escala)|(centro)|(altura)|(radio)', b):
          idem += str(nlinea)+a+'\n'
        if re.findall('Definir', b):
          definir += str(nlinea)+' '+a+'\n'
        if re.findall('Rotar', b):
          rotar+= str(nlinea)+' '+a+'\n'
        if re.findall('Escalar', b):
          escalar+= str(nlinea)+' '+a+'\n'
        if re.findall('Colorear', b):
          color+= str(nlinea)+' '+a+'\n'
        if re.findall('Trasladar', b):
          trasladar+= str(nlinea)+' '+a+'\n'
        if re.findall('Dibujar', b):
          dibujar += str(nlinea)+' '+a+'\n'

  return c, rotar, escalar, color, trasladar, dibujar, idem, definir
  
#función que extrae el identificador y el valor a rotar
def rotar(lineas):
  lineas=lineas
  j=0
  r=[]
  for a in lineas:
    palabras = a.split(' ')
    id=v=' '
    i=p=n=0
    for b in palabras:
      if re.findall('[\-]?[0-9]{1,}(\.[0-9]{1,})?', b) and p==0:
        p=1
        n=b
      if re.findall('[a-z]+[\d]+', b):
        id=b
      if re.findall('[\-]?[0-9]{1,}(\.[0-9]{1,})?', b) and i==1:
        v=b
        r.append([])
        r[j].append(id)
        r[j].append(v)
        r[j].append(n)
        j+=1
      if re.findall('hasta', b):
        i=1
  return r

#función que extrae el identificador y e valor deescalar 
def escalar(lineas):
  lineas=lineas
  e=[]
  j=0
  for a in lineas:
    palabras = a.split(' ')
    id=v=' '
    i=p=n=0
    for b in palabras:
      if re.findall('[\-]?[0-9]{1,}(\.[0-9]{1,})?', b) and p==0:
        p=1
        n=b
      if re.findall('[a-z]+[\d]+', b):
        id=b
      if re.findall('[\-]?[0-9]{1,}(\.[0-9]{1,})?', b) and i==1:
        v=b
        e.append([])
        e[j].append(id)
        e[j].append(v)
        e[j].append(n)
        j+=1
      if re.findall('hasta', b):
        i=1

  return e
  
#función que extrae el identificador y su color
def color(lineas):
  lineas=lineas
  c=[]
  c1=[]
  k=j=0
  for a in lineas:
    palabras = a.split(' ')
    bf=id=color=' '
    i=p=n=0
    for b in palabras:
      if re.findall('[0-9]*', b) and p==0:
        n=b
        p=1
      if re.findall('(borde)|(fondo)', b):
        bf=b
      if re.findall('[a-z]+[\d]+', b):
        id=b
      if re.findall('([rR]ojo)|([aA]zul)|([aA]marillo)|([vV]erde)|([mM]orado)|([gG]ris)|([nN]egro)|([nN]aranja)|([mM]arron)|([rR]osado)', b) and i==1:
        color=b
        if bf == 'borde':
          c.append([])
          c[j].append(id)
          c[j].append(color)
          c[j].append(n)
          j+=1
        if bf=='fondo':
          c1.append([])
          c1[k].append(id)
          c1[k].append(color)
          c1[k].append(n)
          k+=1
      if re.findall('de', b):
        i=1

  return c, c1
  
#función que extrae el identificador y e valor trasladar (x, y)
def trasladar(lineas):
  lineas=lineas
  t_x=[]
  t_y=[]
  j=k=0
  for a in lineas:
    palabras = a.split(' ')
    x=id=v=' '
    i=p=n=0
    for b in palabras:
      if re.findall('[\-]?[0-9]{1,}(\.[0-9]{1,})?', b) and p==0:
        p=1
        n=b
      if re.findall('(x)|(y)', b):
        x=b
      if re.findall('[a-z]+[\d]+', b):
        id=b
      if re.findall('[\-]?[0-9]{1,}(\.[0-9]{1,})?', b) and i==1:
        v=b
        if x=='x':
          t_x.append([])
          t_x[j].append(id)
          t_x[j].append(v)
          t_x[j].append(n)
          j+=1
        if x=='y':
          t_y.append([])
          t_y[k].append(id)
          t_y[k].append(v)
          t_y[k].append(n)
          k+=1
      if re.findall('hasta', b):
        i=1
  return t_x, t_y
  
#función que extrae el identificador y si se va a dibujar
def dibujar(lineas):
  lineas=lineas
  d=[]
  j=0

  for a in lineas:
    palabras = a.split(' ')
    id=' '
    v=p=0
    for b in palabras:
      if re.findall('[\-]?[0-9]{1,}(\.[0-9]{1,})?', b) and p==0:
        v=b
        p=1
      if re.findall('[a-z]+[\d]+', b):
        id=b
        d.append([])
        d[j].append(id)
        d[j].append(v)
        j+=1

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
  P={}
  
  for a in lineas:
    palabras = a.split(' ')
    id=x=v=var=' '
    p=i=t=0
    for b in palabras:
      if re.findall('#', b):
        t=1
      if t==0:
        if re.findall('(extremo)|(potencia)', b):
          var=b
        if re.findall('(A)|(B)', b):
          x=b
        if re.findall('[a-z]+[\d]+', b) and p==0:
          id=b
          p=1
        if re.findall('[\-]?[0-9]{1,}(\.[0-9]{1,})?', b) and i==2 and var=='potencia':
          P[id]=b
        if re.findall('[a-z]+[\d]+', b) and i==2 and var=='extremo':
          v=b
          if x=='A':
            A[id]=v
          if x=='B':
            B[id]=v
        if re.findall('asignar', b):
          i=2
          
  return A, B, P

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
  lcoordenada=lextremo=lvertice=lsemiEje=lcirculo=lcuadrado=lhiper=lparabola=lcono=lesfera=lcilindro=lcurva=' '
  Coordenada={}
  Extremo={}
  Curva={}
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
      if tipos[key]=='Recta' :
        if re.findall('extremo', b):
          lextremo+=b+'\n'
      if tipos[key]=='Curva':
        if re.findall('(extremo)|(potencia)', b):
          lcurva+=b+'\n'
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
  lcurva = lcurva.splitlines()
  Curva = extremo(lcurva)
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

  return Coordenada, Extremo, Vertice, Elipse, Circulo, Cuadrado, Hiperbola, Parabola, Cono, Esfera, Cilindro, Curva

#función que devuelve una tabla con todos los identificadores y sus atributos de 2D y 3d
def simbolos(data, lineas):
  data=data
  lineas=lineas

  identificadores = tabla(data, lineas)
  Atributos = atributos(lineas, identificadores[0])
  
  keys = identificadores[0]
  simbolos=[]
  for i in range(len(keys)):
    simbolos.append([])
    simbolos[i].append(i)

  os.system('rm .erroresLexico.cg')
  e = semantic(keys, identificadores[6], identificadores[7])
  i=0
  f = open('.erroresLexico.cg', 'a')
  for key in keys.keys():
    simbolos[i].append(key)
    simbolos [i].append(keys[key])
    if keys[key]=='Punto':
      coord = Atributos[0]
      if coord[0].has_key(key)==True:
        simbolos[i].append(coord[0][key])
      else:
        f.write('La coordenada x del '+str(key)+', no tiene valor'+'\n')
        e=1
      if coord[1].has_key(key)==True:
        simbolos[i].append(coord[1][key])
      else:
        f.write('La coordenada y del '+str(key)+', no tiene valor'+'\n')
        e=1
    if keys[key]=='Recta':
      sec = Atributos[1]
      if sec[0].has_key(key)==True:
        simbolos[i].append(sec[0][key])
      else:
        f.write('El extremo A de la '+str(key)+', no tiene valor'+'\n')
        e=1
      if sec[1].has_key(key)==True:
        simbolos[i].append(sec[1][key])
      else:
        f.write('El extremo B de la '+str(key)+', no tiene valor'+'\n')
        e=1
    if keys[key]=='Curva':
      sec = Atributos[11]
      if sec[0].has_key(key)==True:
        simbolos[i].append(sec[0][key])
      else:
        f.write('El extremo A de la '+str(key)+', no tiene valor'+'\n')
        e=1
      if sec[1].has_key(key)==True:
        simbolos[i].append(sec[1][key])
      else:
        f.write('El extremo B de la '+str(key)+', no tiene valor'+'\n')
        e=1
      if sec[2].has_key(key)==True:
        simbolos[i].append(sec[2][key])
      else:
        f.write('La potencia de la '+str(key)+', no tiene valor'+'\n')
        e=1
    if keys[key]=='Triangulo':
      vert = Atributos[2]
      if vert[0].has_key(key)==True:
        simbolos[i].append(vert[0][key])
      else:
        f.write('El Vertice A del '+str(key)+', no tiene valor'+'\n')
        e=1
      if vert[1].has_key(key)==True:
        simbolos[i].append(vert[1][key])
      else:
        f.write('El Vertice B del '+str(key)+', no tiene valor'+'\n')
        e=1
      if vert[2].has_key(key)==True:
        simbolos[i].append(vert[2][key])
      else:
        f.write('El Vertice C del '+str(key)+', no tiene valor'+'\n')
        e=1
    if keys[key]=='Elipse':
      elip = Atributos[3]
      if elip[0].has_key(key)==True:
        simbolos[i].append(elip[0][key])
      else:
        f.write('El semieje A de la '+str(key)+', no tiene valor'+'\n')
        e=1
      if elip[1].has_key(key)==True:
        simbolos[i].append(elip[1][key])
      else:
        f.write('El semieje B de la '+str(key)+', no tiene valor'+'\n')
        e=1
      if elip[2].has_key(key)==True:
        simbolos[i].append(elip[2][key])
      else:
        f.write('El centro de la '+str(key)+', no tiene valor'+'\n')
        e=1
    if keys[key]=='Circunferencia':
      cir = Atributos[4]
      if cir[0].has_key(key)==True:
        simbolos[i].append(cir[0][key])
      else:
        f.write('El radio de la '+str(key)+', no tiene valor'+'\n')
        e=1
      if cir[1].has_key(key)==True:
        simbolos[i].append(cir[1][key])
      else:
        f.write('El centro de la '+str(key)+', no tiene valor'+'\n')
        e=1
    if keys[key]=='Cuadrilatero':
      cuad = Atributos[5]
      if cuad[0].has_key(key)==True:
        simbolos[i].append(cuad[0][key])
      else:
        f.write('El Vertice A de '+str(key)+', no tiene valor'+'\n')
        e=1
      if cuad[1].has_key(key)==True:
        simbolos[i].append(cuad[1][key])
      else:
        f.write('El Vertice B de '+str(key)+', no tiene valor'+'\n')
        e=1
      if cuad[2].has_key(key)==True:
        simbolos[i].append(cuad[2][key])
      else:
        f.write('El Vertice C de '+str(key)+', no tiene valor'+'\n')
        e=1
      if cuad[3].has_key(key)==True:
        simbolos[i].append(cuad[3][key])
      else:
        f.write('El Vertice D de '+str(key)+', no tiene valor'+'\n')
        e=1
    if keys[key]=='Hiperbola':
      hipe = Atributos[6]
      if hipe[0].has_key(key)==True:
        simbolos[i].append(hipe[0][key])
      else:
        f.write('El semieje A de '+str(key)+', no tiene valor'+'\n')
        e=1
      if hipe[1].has_key(key)==True:
        simbolos[i].append(hipe[1][key])
      else:
        f.write('El semieje B de '+str(key)+', no tiene valor'+'\n')
        e=1
      if hipe[2].has_key(key)==True:
        simbolos[i].append(hipe[2][key])
      else:
        f.write('El centro de '+str(key)+', no tiene valor'+'\n')
        e=1
    if keys[key]=='Parabola':
      para = Atributos[7]
      if para[0].has_key(key)==True:
        simbolos[i].append(para[0][key])
      else:
        f.write('La escala D de '+str(key)+', no tiene valor'+'\n')
        e=1
      if para[1].has_key(key)==True:
        simbolos[i].append(para[1][key])
      else:
        f.write('El origen de '+str(key)+', no tiene valor'+'\n')
        e=1
    if keys[key]=='Cono':
      cono = Atributos[8]
      if cono[0].has_key(key)==True:
        simbolos[i].append(cono[0][key])
      else:
        f.write('El radio de '+str(key)+', no tiene valor'+'\n')
        e=1
      if cono[1].has_key(key)==True:
        simbolos[i].append(cono[1][key])
      else:
        f.write('La altura de '+str(key)+', no tiene valor'+'\n')
        e=1
      if cono[2].has_key(key)==True:
        simbolos[i].append(cono[2][key])
      else:
        f.write('El centro de '+str(key)+', no tiene valor'+'\n')
        e=1
    if keys[key]=='Esfera':
      esf = Atributos[9]
      if esf[0].has_key(key)==True:
        simbolos[i].append(esf[0][key])
      else:
        f.write('El centro de '+str(key)+', no tiene valor'+'\n')
        e=1
      if esf[1].has_key(key)==True:
        simbolos[i].append(esf[1][key])
      else:
        f.write('El radio de '+str(key)+', no tiene valor'+'\n')
        e=1
    if keys[key]=='Cilindro':
      cil = Atributos[10]
      if cil[0].has_key(key)==True:
        simbolos[i].append(cil[0][key])
      else:
        f.write('El radio de '+str(key)+', no tiene valor'+'\n')
        e=1
      if cil[1].has_key(key)==True:
        simbolos[i].append(cil[1][key])
      else:
        f.write('La altura de '+str(key)+', no tiene valor'+'\n')
        e=1
      if cil[2].has_key(key)==True:
        simbolos[i].append(cil[2][key])
      else:
        f.write('El centro de '+str(key)+', no tiene valor'+'\n')
        e=1
    i=i+1

  f.close()
  if e==0:
    os.system('rm .erroresLexico.cg')

  """
    Se genera 2 tablas:
    la primera tabla "simbolo" contiene los valores de las corrdenadas, aristas, secmentos, centro, radio, origen, .... y  tiene el siguiente orden:
        Posición Identificador Tipo A B C D
    para el punto A=X, B=y
    para la circunferencia y la esfera radio =A, centro=B
    para la elipse y la hiperbola centro=C, semiEje A=A, semiEje=B
    para la parabola escala=A, centro = B
    para el cono y el cilindro radio=A, altura=B, centro=C 
    la segunda tabla "tabladibujar" contiene las figuras a graficar y tiene el siguiente orden:
        identificador Rotar Escalar Trasladar X Trasladar Y Color liniea posicióndegraficar
-- es importante saber que para definir Escalar debe hacerse de la siguiente forma:
Escalar triangulo1 hasta 3 veces : 
para no tener problemas si sean reconocido
  """
  Tabladibujar = tabladibujar(identificadores)
  return simbolos, Tabladibujar

def tabladibujar(identificadores):
  identificadores = identificadores
  i=0
  tipo = identificadores[0]
  lrotar = identificadores[1].splitlines()
  lescalar = identificadores[2].splitlines()
  lcolor = identificadores[3].splitlines()
  ltrasladar = identificadores[4].splitlines()
  ldibujar = identificadores[5].splitlines()
  Rotar = rotar(lrotar)
  Escalar = escalar(lescalar)
  Trasladar = trasladar(ltrasladar)
  TrasladarX = Trasladar[0]
  TrasladarY = Trasladar[1]
  Color = color(lcolor)
  color1 = Color[0]
  color2 = Color[1]
  Dibujar = dibujar(ldibujar)
  tabladibujar=[]
  for k in Dibujar:
    tabladibujar.append([])
    tabladibujar[i].append(k[0])
    tabladibujar[i].append(0) #rotar
    tabladibujar[i].append(0) #escalar
    tabladibujar[i].append(0) #trasladar x
    tabladibujar[i].append(0) #trasladar y
    tabladibujar[i].append(0) #color de borde
    tabladibujar[i].append(0) #color de fondo
    tabladibujar[i].append(k[1]) #posición
    i+=1
  d=len(Dibujar)
  tam={}
  for i in range(d-1):
    tam[tabladibujar[i][0]]='1'

  print len(tam)
  min=0
  for i in range(d):
    min=0
    for j in range(len(Rotar)):
        if Rotar[j][0]==tabladibujar[i][0]:
          if Rotar[j][2]>min and Rotar[j][2]<tabladibujar[i][7]:
            tabladibujar[i][1]=Rotar[j][1]
            min=tabladibujar[i][7]
  min=0
  for i in range(d):
    min=0
    for j in range(len(Escalar)):
        if Escalar[j][0]==tabladibujar[i][0]:
          if Escalar[j][2]>min and Escalar[j][2]<tabladibujar[i][7]:
            tabladibujar[i][2]=Escalar[j][1]
            min=tabladibujar[i][7]
  min=0
  for i in range(d):
    min=0
    for j in range(len(TrasladarX)):
        if TrasladarX[j][0]==tabladibujar[i][0]:
          if TrasladarX[j][2]>min and TrasladarX[j][2]<tabladibujar[i][7]:
            tabladibujar[i][3]=TrasladarX[j][1]
            min=tabladibujar[i][7]
  min=0
  for i in range(d):
    min=0
    for j in range(len(TrasladarY)):
        if TrasladarY[j][0]==tabladibujar[i][0]:
          if TrasladarY[j][2]>min and TrasladarY[j][2]<tabladibujar[i][7]:
            tabladibujar[i][4]=TrasladarY[j][1]
            min=tabladibujar[i][7]
  min=0
  for i in range(d):
    if len(tam)>3:
      min=0
    for j in range(len(color1)):
        if color1[j][0]==tabladibujar[i][0]:
          if color1[j][2]>min and color1[j][2]<tabladibujar[i][7]:
            tabladibujar[i][5]=color1[j][1]
            min=tabladibujar[i][7]
  min=0
  for i in range(d):
    if len(tam)>3:
      min=0
    for j in range(len(color2)):
        if color2[j][0]==tabladibujar[i][0]:
          if color2[j][2]>min and color2[j][2]<tabladibujar[i][7]:
            tabladibujar[i][6]=color2[j][1]
            min=tabladibujar[i][7]

  return tabladibujar

def nombre(self, label):
    label = label
    palabras = label.split('/')
    archivo=' '
    for a in palabras:
      print a
      if re.findall('[\W]+[.CG]', a):
        archivo=a

    return archivo
    
def preferencias(self):
    atributos = []
    archivo = ['.preferencias.dat']
    lineas=' '
    for texto in archivo:
      f = open(texto, 'r')
      data = f.read()
      lineas = data.splitlines()
      f.close()

    for line in lineas:
      atributos = line.split(' ')
      
    return atributos

def semantic(key, idem, definir):
    key = key
    idem = idem
    definir = definir
    declarado={}
    id=' '
    e=0
    idem = idem.splitlines()
    definir = definir.splitlines()
    t=[]
    j=0
    for d in definir:
      p=n=0
      id=tipo=' '
      palabras = d.split(' ')
      for a in palabras:
        if re.findall('[1-9]*', a) and p==0:
          n=a
          p=1
        if re.findall('[a-z]+[\d]+', a):
          id=a
        if re.findall('((Punto)|(Recta)|(Parabola)|(Hiperbola)|(SemiRecta)|(Segmento)|(Curva)|(Circunferencia)|(Cuadrilatero)|(Triangulo)|(Cono)|(Esfera)|(Elipse)|(Cilindro))', a):
          tipo=a
          t.append([])
          t[j].append(n)
          t[j].append(tipo)
          t[j].append(id)
          j+=1

    d={}
    n=len(t)
    for a in range(n-1):
      for b in range(a+1, n-1):
        if t[a][2]==t[b][2]:
          d[str(t[a][2])] = str(t[b][0])

    A=[]
    j=0
    for a in idem:
      pala = a.split(' ')
      r=p=q=s=n=0
      id=atri=' '
      for b in pala:
        if s==0:
          if re.findall('[0-9]*', b) and p==0:
            n=b
            p=1
          if re.findall('(coordenada)|(extremo)|(vertice)|(semiEje)|(potencia)|(origen)|(escala)|(centro)|(altura)|(radio)', b):
            atri=b
          if re.findall('[a-z]+[\d]+', b):
            id = b
          if re.findall('de', b):
            q = 1
          if re.findall('asignar', b):
            s=1
        for c in t:
          if c[2]==id and c[0]<n:
            r=r+1
        declarado[id]=r
      if key.has_key(id)==True:
        if (key[id]=='Punto' and atri!='coordenada') or (key[id]=='Recta' and atri!='extremo') or (key[id]=='Triangulo' and atri!='vertice') or (key[id]=='Cuadrilatero' and atri!='vertice') or (key[id]=='Circunferencia'  and atri=='coordenada') or (key[id]=='Circunferencia' and atri=='extremo') or (key[id]=='Circunferencia' and atri=='vertice') or (key[id]=='Circunferencia' and atri=='semiEje') or (key[id]=='Circunferencia' and atri=='potencia') or (key[id]=='Circunferencia' and atri=='origen') or (key[id]=='Circunferencia' and atri=='escala') or (key[id]=='Circunferencia' and atri=='altura') or (key[id]=='Curva'  and atri=='coordenada') or  (key[id]=='Curva' and atri=='vertice') or (key[id]=='Curva' and atri=='semiEje') or (key[id]=='Curva' and atri=='origen') or (key[id]=='Curva' and atri=='escala') or (key[id]=='Curva' and atri=='altura') or (key[id]=='Curva' and atri=='centro') or (key[id]=='Curva' and atri=='radio') or (key[id]=='Hiperbola'  and atri=='coordenada') or (key[id]=='Hiperbola' and atri=='extremo') or (key[id]=='Hiperbola' and atri=='vertice') or (key[id]=='Hiperbola' and atri=='potencia') or (key[id]=='Hiperbola' and atri=='origen') or (key[id]=='Hiperbola' and atri=='escala') or (key[id]=='Hiperbola' and atri=='altura') or (key[id]=='Hiperbola' and atri=='radio') or (key[id]=='Parabola'  and atri=='coordenada') or (key[id]=='Parabola' and atri=='extremo') or (key[id]=='Parabola' and atri=='vertice') or (key[id]=='Parabola' and atri=='semiEje') or (key[id]=='Parabola' and atri=='potencia') or (key[id]=='Parabola' and atri=='altura') or (key[id]=='Parabola' and atri=='centro') or (key[id]=='Parabola' and atri=='radio') or (key[id]=='Elipse'  and atri=='coordenada') or (key[id]=='Elipse' and atri=='extremo') or (key[id]=='Elipse' and atri=='vertice') or (key[id]=='Elipse' and atri=='potencia') or (key[id]=='Elipse' and atri=='origen') or (key[id]=='Elipse' and atri=='escala') or (key[id]=='Elipse' and atri=='altura') or (key[id]=='Elipse' and atri=='radio') or (key[id]=='Esfera'  and atri=='coordenada') or (key[id]=='Esfera' and atri=='extremo') or (key[id]=='Esfera' and atri=='vertice') or (key[id]=='Esfera' and atri=='semiEje') or (key[id]=='Esfera' and atri=='potencia') or (key[id]=='Esfera' and atri=='origen') or (key[id]=='Esfera' and atri=='escala') or (key[id]=='Esfera' and atri=='altura') or (key[id]=='Cono'  and atri=='coordenada') or (key[id]=='Cono' and atri=='extremo') or (key[id]=='Cono' and atri=='vertice') or (key[id]=='Cono' and atri=='semiEje') or (key[id]=='Cono' and atri=='potencia') or (key[id]=='Cono' and atri=='origen') or (key[id]=='Cono' and atri=='escala') or (key[id]=='Cilindro'  and atri=='coordenada') or (key[id]=='Cilindro' and atri=='extremo') or (key[id]=='Cilindro' and atri=='vertice') or (key[id]=='Cilindro' and atri=='semiEje') or (key[id]=='Cilindro' and atri=='potencia') or (key[id]=='Cilindro' and atri=='origen') or (key[id]=='Cilindro' and atri=='escala'):
          A.append([])
          A[j].append(id)
          A[j].append(atri)
          A[j].append(n)
          j += 1

    for key in declarado.keys():
      if declarado[key] == 0:
        if key!=' ':
          f = open('.erroresLexico.cg', 'a')
          f.write('El identificador '+str(key)+', no esta declarado.'+'\n')
          f.close()
          e=1

    for key in d.keys():
      f = open('.erroresLexico.cg', 'a')
      f.write("El identificador "+str(key)+", fue declarado mas de una vez"+"\n")
      f.close()
      e=1

    for k in A:
      f = open('.erroresLexico.cg', 'a')
      f.write('El identificador '+str(k[0])+', en la linea '+str(k[2])+', se le asignó un atributo que no corresponde a su tipo'+'\n')
      f.close()
      e=1

    return e
