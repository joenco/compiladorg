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
    print a[1]+"\t\t"+a[2]
    if (a[2]== "Punto"):
      if (int(a[10]) == 1 ):
        punto(float(a[3]),float(a[4]),float(a[7]),float(a[8]),obtener_color(str(a[9])))
    elif (a[2]=="Recta"):
      if (int(a[10]) == 1 ):
        # Atributos: x1, y1, x2, y2, rotar, escalar, trasladarx, trasladary, color
        recta(obtener_x(a[3], simbolos),obtener_y(a[3], simbolos),obtener_x(a[4], simbolos),obtener_y(a[4], simbolos),int(a[5]),int(a[6]),float(a[7]),float(a[8]),obtener_color(a[9]))
    elif (a[2]=="Triangulo"):
      if(int(a[11])==1):
        #Atributos: simbolos, p1, p2, p3,rotar,escalar,tx,ty, color
        triangulo(simbolos,a[3],a[4],a[5],int(a[6]),int(a[7]),float(a[8]),float(a[9]),obtener_color(a[10]))
    elif (a[2] == "Cuadrilatero"):
      if(int(a[12])==1):      
        #Atributos: simbolos, p1, p2, p3, p4,rotar, escalar, tx, ty, color
        cuadrilatero(simbolos,a[3],a[4],a[5],a[6],int(a[7]),int(a[8]),float(a[9]),float(a[10]),obtener_color(a[11]))  
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
  
#Plantilla punto
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

#Plantilla triangulo
def triangulo(simbolos,p1,p2,p3,rotar,escalar,tx,ty,color):
  x1 = obtener_x(p1,simbolos)
  y1 = obtener_y(p1,simbolos)
  x2 = obtener_x(p2,simbolos)
  y2 = obtener_y(p2,simbolos)
  x3 = obtener_x(p3,simbolos)
  y3 = obtener_y(p3,simbolos)

  #Trasladar triangulo
  x1 = x1*44 + tx*44
  y1 = y1*44 + ty*44  
  x2 = x2*44 + tx*44
  y2 = y2*44 + ty*44
  x3 = x3*44 + tx*44
  y3 = y3*44 + ty*44

  #Dibujar triangulo
  turtle.penup()
  turtle.setposition(x1,y1)
  turtle.pendown()
  turtle.color(color)
  turtle.pensize(8)
  turtle.setposition(x2,y2)
  turtle.setposition(x3,y3)
  turtle.setposition(x1,y1)
  
  #Calculos de lados
  a =  math.sqrt(((x2 -x1)**2)+((y2-y1)**2)) #Opuesto de p3
  b =  math.sqrt(((x3 -x1)**2)+((y3-y1)**2)) #Opuesto de p2
  c =  math.sqrt(((x3 -x2)**2)+((y3-y2)**2)) #Opuesto de p1

  #Calculo de incentro
  incentro_x = (( (x1*c) + (x2*b) + (x3*a) ) / (a+b+c) )
  incentro_y = (( (y1*c) + (y2*b) + (y3*a) ) / (a+b+c) ) 

  #Calculo de distancias
  d1 = math.sqrt(((incentro_x -x1)**2)+((incentro_y-y1)**2))
  d2 = math.sqrt(((incentro_x -x2)**2)+((incentro_y-y2)**2))
  d3 = math.sqrt(((incentro_x -x3)**2)+((incentro_y-y3)**2))

  #Calculo de angulos
  turtle.penup()  
  turtle.setposition(incentro_x, incentro_y)
  a1 = turtle.towards(x1,y1)
  a2 = turtle.towards(x2,y2)
  a3 = turtle.towards(x3,y3)

  #Calcular nuevos puntos para escalar
  turtle.setposition(incentro_x, incentro_y)
  turtle.setheading(0)
  turtle.lt(a1)
  turtle.forward(d1*escalar)
  x_1 = turtle.xcor()
  y_1 = turtle.ycor()

  turtle.setposition(incentro_x, incentro_y)
  turtle.setheading(0)
  turtle.lt(a2)
  turtle.forward(d2*escalar)
  x_2 = turtle.xcor()
  y_2 = turtle.ycor()
   
  turtle.setposition(incentro_x, incentro_y)
  turtle.setheading(0)
  turtle.lt(a3)
  turtle.forward(d3*escalar)
  x_3 = turtle.xcor()
  y_3 = turtle.ycor()

  #Calcular nuevos puntos para rotar
  turtle.setposition(incentro_x, incentro_y)
  turtle.setheading(0)
  turtle.lt(a1+rotar)
  turtle.forward(d1)
  x_1_ = turtle.xcor()
  y_1_ = turtle.ycor()

  turtle.setposition(incentro_x, incentro_y)
  turtle.setheading(0)
  turtle.lt(a2+rotar)
  turtle.forward(d2)
  x_2_ = turtle.xcor()
  y_2_ = turtle.ycor()
   
  turtle.setposition(incentro_x, incentro_y)
  turtle.setheading(0)
  turtle.lt(a3+rotar)
  turtle.forward(d3)
  x_3_ = turtle.xcor()
  y_3_ = turtle.ycor()

  #Rotar triangulo
  if rotar != 0:
    print "rotar"
    turtle.color("#008080")
    turtle.penup()
    turtle.setposition(x_1_,y_1_)
    turtle.pendown()
    turtle.setposition(x_2_,y_2_)
    turtle.setposition(x_3_,y_3_)
    turtle.setposition(x_1_,y_1_)
     
  #Escalar recta
  if escalar != 0:
    print "escalar"
    turtle.color("#00FFFF")
    turtle.penup()
    turtle.setposition(x_1,y_1)
    turtle.pendown()
    turtle.setposition(x_2,y_2)
    turtle.setposition(x_3,y_3)
    turtle.setposition(x_1,y_1)

#Plantilla cuadrilatero
def cuadrilatero(simbolos,p1,p2,p3,p4,rotar,escalar,tx,ty,color):

  #Obtener coordenadas
  x1 = obtener_x(p1,simbolos)*44
  y1 = obtener_y(p1,simbolos)*44
  x2 = obtener_x(p2,simbolos)*44
  y2 = obtener_y(p2,simbolos)*44
  x3 = obtener_x(p3,simbolos)*44
  y3 = obtener_y(p3,simbolos)*44
  x4 = obtener_x(p4,simbolos)*44
  y4 = obtener_y(p4,simbolos)*44

  #Trasladar cuadrilatero
  x1 = x1 + tx*44
  y1 = y1 + ty*44  
  x2 = x2 + tx*44
  y2 = y2 + ty*44
  x3 = x3 + tx*44
  y3 = y3 + ty*44
  x4 = x4 + tx*44
  y4 = y4 + ty*44	

  #Caucular punto medio de cuadrilatero
  x5 = inferior_izquierdo(x1,x2,x3,x4,y1,y2,y3,y4,0)
  y5 = inferior_izquierdo(x1,x2,x3,x4,y1,y2,y3,y4,1)
  x6 = superior_derecho(x1,x2,x3,x4,y1,y2,y3,y4,0)
  y6 = superior_derecho(x1,x2,x3,x4,y1,y2,y3,y4,1)
  punto_medio_x = (x5 + x6) / 2 
  punto_medio_y = (y5 + y6) / 2

  print punto_medio_x, punto_medio_y

  #Calculo de distancias
  d1 = math.sqrt(((punto_medio_x -x1)**2)+((punto_medio_y-y1)**2))
  d2 = math.sqrt(((punto_medio_x -x2)**2)+((punto_medio_y-y2)**2))
  d3 = math.sqrt(((punto_medio_x -x3)**2)+((punto_medio_y-y3)**2))
  d4 = math.sqrt(((punto_medio_x -x4)**2)+((punto_medio_y-y4)**2))
  
  #Calculo de angulos
  turtle.penup()  
  turtle.setposition(punto_medio_x, punto_medio_y)
  a1 = turtle.towards(x1,y1)
  a2 = turtle.towards(x2,y2)
  a3 = turtle.towards(x3,y3)
  a4 = turtle.towards(x4,y4)

  #Calcular nuevos puntos para escalar
  turtle.setposition(punto_medio_x, punto_medio_y)
  turtle.setheading(0)
  turtle.lt(a1)
  turtle.forward(d1*escalar)
  x_1 = turtle.xcor()
  y_1 = turtle.ycor()

  turtle.setposition(punto_medio_x, punto_medio_y)
  turtle.setheading(0)
  turtle.lt(a2)
  turtle.forward(d2*escalar)
  x_2 = turtle.xcor()
  y_2 = turtle.ycor()
   
  turtle.setposition(punto_medio_x, punto_medio_y)
  turtle.setheading(0)
  turtle.lt(a3)
  turtle.forward(d3*escalar)
  x_3 = turtle.xcor()
  y_3 = turtle.ycor()

  turtle.setposition(punto_medio_x, punto_medio_y)
  turtle.setheading(0)
  turtle.lt(a4)
  turtle.forward(d4*escalar)
  x_4 = turtle.xcor()
  y_4 = turtle.ycor()

  #Calcular nuevos puntos para rotar
  turtle.setposition(punto_medio_x, punto_medio_y)
  turtle.setheading(0)
  turtle.lt(a1+rotar)
  turtle.forward(d1)
  x_1_ = turtle.xcor()
  y_1_ = turtle.ycor()

  turtle.setposition(punto_medio_x, punto_medio_y)
  turtle.setheading(0)
  turtle.lt(a2+rotar)
  turtle.forward(d2)
  x_2_ = turtle.xcor()
  y_2_ = turtle.ycor()
   
  turtle.setposition(punto_medio_x, punto_medio_y)
  turtle.setheading(0)
  turtle.lt(a3+rotar)
  turtle.forward(d3)
  x_3_ = turtle.xcor()
  y_3_ = turtle.ycor()

  turtle.setposition(punto_medio_x, punto_medio_y)
  turtle.setheading(0)
  turtle.lt(a4+rotar)
  turtle.forward(d4)
  x_4_ = turtle.xcor()
  y_4_ = turtle.ycor()

  #Dibujar cuadrilatero
  turtle.color(color)         
  turtle.penup()
  turtle.setposition(x1,y1)
  turtle.pendown()
  turtle.pensize(8)
  turtle.setposition(x2,y2)
  turtle.setposition(x3,y3)
  turtle.setposition(x4,y4)
  turtle.setposition(x1,y1)

  #Escalar
  if escalar != 0:
    print "escalar"
    turtle.color("#00FFFF")
    turtle.penup()
    turtle.setposition(x_1,y_1)
    turtle.pendown()
    turtle.setposition(x_2,y_2)
    turtle.setposition(x_3,y_3)
    turtle.setposition(x_4,y_4)
    turtle.setposition(x_1,y_1)

  #Rotar
  if rotar != 0:
    print "rotar"
    turtle.color("#008080")
    turtle.penup()
    turtle.setposition(x_1_,y_1_)
    turtle.pendown()
    turtle.setposition(x_2_,y_2_)
    turtle.setposition(x_3_,y_3_)
    turtle.setposition(x_4_,y_4_)
    turtle.setposition(x_1_,y_1_)

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

def inferior_izquierdo(x1,x2,x3,x4,y1,y2,y3,y4,c):
  inferior_x = x1
  inferior_y = y1
  if (inferior_x >= x2 and inferior_y >= y2):
    inferior_x = x2
    inferior_y = y2 
  if (inferior_x >= x3 and inferior_y >= y3):
    inferior_x = x3
    inferior_y = y3 
  if (inferior_x >= x4 and inferior_y >= y4):
    inferior_x = x4
    inferior_y = y4 
  if c == 0:
    return inferior_x
  elif c == 1:
    return inferior_y

def superior_derecho(x1,x2,x3,x4,y1,y2,y3,y4,c):
  superior_x = x1
  superior_y = y1
  if (superior_x <= x2 and superior_y <= y2):
    superior_x = x2
    superior_y = y2 
  if (superior_x <= x3 and superior_y <= y3):
    superior_x = x3
    superior_y = y3 
  if (superior_x <= x4 and superior_y <= y4):
    superior_x = x4
    superior_y = y4 
  if c == 0:
    return superior_x
  elif c == 1:
    return superior_y

