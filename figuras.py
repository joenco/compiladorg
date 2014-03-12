import turtle
import math

def dibujar(simbolos):
  simbolos = simbolos

  turtle.shape("turtle")
  turtle.title("Graficos - Compilador Geometrico")
  turtle.speed(0)
  turtle.hideturtle()

  plano2d()

  print "Tabla de Simbolos: ",simbolos
  print "Indentificador\tTipo"
  for a in simbolos:
    if (a[2]== "Punto"):
      print a[1]+"\t\t"+a[2]
      #Dibujar
      if (int(a[10]) == 1 ):
        punto(float(a[3]),float(a[4]),float(a[7]),float(a[8]),obtener_color(str(a[9])))

  turtle.exitonclick()

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
  
def punto(x,y,tx,ty,color):
  x = x
  y = y
  x = x*44 + tx*44
  y = y*44 + ty*44
  turtle.penup()
  turtle.setposition(x,y)
  turtle.pendown()
  turtle.dot(20,color)

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
