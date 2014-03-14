import turtle
import math

#Funcion principal
def dibujar(simbolos):
  simbolos = simbolos

  turtle.shape("turtle")
  turtle.title("Graficos - Compilador Geometrico")
  turtle.speed(0)
  turtle.hideturtle()

  plano2d()

  #Tabla de simbolos
  print "Tabla de Simbolos: ",simbolos
  #Identificadores procesados
  print "Indentificador\tTipo"
  #Recorriendo la tabla de simbolos
  for a in simbolos:
    if (a[2]== "Punto"):
      print a[1]+"\t\t"+a[2]
      #Dibujar
      if (int(a[10]) == 1 ):
        punto(float(a[3]),float(a[4]),float(a[7]),float(a[8]),obtener_color(str(a[9])))
    elif (a[2]=="Recta"):
      if (int(a[10]) == 1 ):
        # Atributos: x1, y1, x2, y2, rotar, escalar, trasladarx, trasladary, color
        recta(obtener_x(a[3], simbolos),obtener_y(a[3], simbolos),obtener_x(a[4], simbolos),obtener_y(a[4], simbolos),int(a[5]),int(a[6]),float(a[7]),float(a[8]),obtener_color(a[9]))
  
  turtle.exitonclick()

#Dibujar plano 2D
def plano2d():
  turtle.penup()

  for i in range(13):
    y = 264 - (44 *i)
    turtle.penup()
    turtle.setposition(-264,y)
    turtle.pendown()
    turtle.forward(528)
  
  turtle.right(90)

  for i in range(13):
    x = -264 + (44*i)
    turtle.penup()
    turtle.setposition(x,264)
    turtle.pendown()
    turtle.forward(528)
  
  turtle.penup()
  turtle.home()
  turtle.pendown()
  turtle.color("blue")         
  turtle.pensize(3)

  for i in range(4):
    grados = 90 * (i+1)
    turtle.home()
    turtle.left(grados)
    turtle.forward(264) 
  
#Dibujar punto
def punto(x,y,tx,ty,color):
  x = x
  y = y
  x = x*44 + tx*44
  y = y*44 + ty*44
  turtle.penup()
  turtle.setposition(x,y)
  turtle.pendown()
  turtle.dot(20,color)

#Plantilla recta
def recta(x1, y1, x2, y2, rotar, escalar, tx, ty, color):
  x1 = x1
  y1 = y1
  x2 = x2 
  y2 = y2
  rotar = rotar
  escalar = escalar

  #Trasladar recta
  x1 = x1*44 + tx*44
  x2 = x2*44 + tx*44
  y1 = y1*44 + ty*44
  y2 = y2*44 + ty*44 

  #Calculos recta
  angulo = int(math.degrees(math.atan2((y2 - y1) , (x2 - x1))))
  punto_medio_x = (x1 + x2) / 2 
  punto_medio_y = (y1 + y2) / 2
  distancia = int (math.sqrt(((x2 -x1)**2)+((y2-y1)**2)))

  print "x1, y1, x2, y2: ",x1,y1,x2,y2
  print "Angulo: ",angulo 
  print "Distancia",distancia

  #Dibujar recta
  turtle.penup()
  turtle.setposition(x1,y1)
  turtle.pendown()
  turtle.color(color)
  turtle.pensize(8)
  turtle.setposition(x2,y2)

  #Rotar recta
  if rotar != 0:
    turtle.color("#008080")
    turtle.penup()
    turtle.setposition(punto_medio_x,punto_medio_y)
    turtle.setheading(0)
    turtle.lt(angulo+rotar)
    turtle.pendown()
    turtle.forward(distancia/2)
    turtle.penup()
    turtle.setposition(punto_medio_x,punto_medio_y)
    turtle.setheading(0)
    turtle.lt(angulo+rotar+180)
    turtle.pendown()
    turtle.forward(distancia/2)

  #Escalar recta
  if escalar != 0:
    turtle.color("#00FFFF")
    turtle.penup()
    turtle.setposition(punto_medio_x,punto_medio_y)
    turtle.setheading(0)
    turtle.lt(angulo)
    turtle.pendown()
    turtle.forward((distancia/2)*escalar)
    turtle.penup()
    turtle.setposition(punto_medio_x,punto_medio_y)
    turtle.setheading(0)
    turtle.lt(angulo+180)
    turtle.pendown()
    turtle.forward((distancia/2)*escalar)
 
#Traducir color a Ingles
def obtener_color(color):
  color = color
  if color == "azul" or color == "Azul":
    color = "blue"
  elif color == "rojo" or color == "Rojo":
    color = "red"
  elif color == "amarillo" or color == "Amarillo":
    color = "yellow"
  elif color == "verde" or color == "Verde":
    color = "green"
  elif color == "morado" or color == "Morado":
    color = "violet"
  elif color == "gris" or color == "Gris":
    color = "gray"
  elif color == "negro" or color == "Negro":
    color = "black"
  elif color == "rosado" or color == "Rosado":
    color = "pink"
  else:
    color = "black"
  return color

#Extraer coordenada x de un punto
def obtener_x(punto, simbolos):
  simbolos = simbolos
  punto = punto
  for a in simbolos:
    if (a[1]== punto):
      return float(a[3])
  return 0

#Extraer coordenada y de un punto
def obtener_y(punto, simbolos):
  simbolos = simbolos
  punto = punto
  for a in simbolos:
    if (a[1]== punto):
      return float(a[4])
  return 0

