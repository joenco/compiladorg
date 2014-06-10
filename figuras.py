import turtle
import math

#Funcion principal
def dibujar(simbolos):
  simbolos = simbolos

  turtle.shape("turtle")
  turtle.title("Graficos - Compilador Geometrico")
  turtle.speed(0)
  turtle.hideturtle()

  print "Tabla 1"
  for i in simbolos[0]:
    print i

  print "Tabla 2"
  for i in simbolos[1]:
    print i

  plano2d()

  #Tabla de simbolos
  #print "Tabla de Simbolos: ",simbolos
  #Identificadores procesados
  #print "Indentificador\tTipo"
  #Recorriendo la tabla de simbolos
  """
  for a in simbolos:
    print a[1]+"\t\t"+a[2]
    if (a[2]== "Punto"):
      if (int(a[10]) == 1 ):
        punto(float(a[3]),float(a[4]),float(a[7]),float(a[8]),obtener_color(str(a[9])))
    elif (a[2]=="Recta"):
      if (int(a[10]) == 1 ):
        # Atributos: x1, y1, x2, y2, rotar, escalar, trasladarx, trasladary, color
        recta(obtener_x(a[3], simbolos),obtener_y(a[3], simbolos),obtener_x(a[4], simbolos),obtener_y(a[4], simbolos),int(a[5]),int(a[6]),float(a[7]),float(a[8]),obtener_color(a[9]))
    elif (a[2]=="Curva"):
      curva()
    elif (a[2]=="Triangulo"):
      if(int(a[11])==1):
        #Atributos: simbolos, p1, p2, p3,rotar,escalar,tx,ty, color
        triangulo(simbolos,a[3],a[4],a[5],int(a[6]),int(a[7]),float(a[8]),float(a[9]),obtener_color(a[10]))
    elif (a[2] == "Cuadrilatero"):
      if(int(a[12])==1):      
        #Atributos: simbolos, p1, p2, p3, p4,rotar, escalar, tx, ty, color
        cuadrilatero(simbolos,a[3],a[4],a[5],a[6],int(a[7]),int(a[8]),float(a[9]),float(a[10]),obtener_color(a[11]))
    elif (a[2]=="Circunferencia"):
      if (int(a[10])==1):
        #Atributo: radio, centro,tx,ty, escalar, color
        circunferencia(simbolos,int(a[3]),a[4],float(a[6]),float(a[7]),float(a[8]),obtener_color(a[9]))  
    elif (a[2]=="Parabola"):
      #if (int(a[10])==1):
        #Atributos: centro
      parabola(simbolos,a[4])
    elif (a[2]=="Elipse"):
      elipse()
    elif (a[2]=="Hiperbola"):
      hiperbola()
  """
  for a in simbolos[1]:
    tip = tipo(a[0],simbolos)
    if tip == "Punto" :
      punto(simbolos,a[0],a[7])
    elif tip == "Recta":
      recta(simbolos,a[0],a[7])
    elif tip == "Curva" :
      curva(simbolos,a[0],a[7])
    elif tip=="Triangulo":
      triangulo(simbolos,a[0],a[7])
    elif tip=="Cuadrilatero":
      cuadrilatero(simbolos,a[0],a[7])
    elif tip=="Circunferencia":
      circunferencia(simbolos,a[0],a[7])
    
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
#def punto(x,y,tx,ty,color):
def punto(simbolos,identificador,linea):
  x = obtener_x(identificador,simbolos)
  y = obtener_y(identificador,simbolos)  

  tx = obtener_tx(identificador, simbolos,linea)
  ty = obtener_ty(identificador, simbolos,linea)
  relleno = obtener_color(obtener_relleno(identificador,simbolos,linea))

  x = x*44 + tx*44
  y = y*44 + ty*44

  turtle.penup() #levantar lapiz
  turtle.setposition(x,y) #ir a posicion
  turtle.pendown() #bajar lapiz
  turtle.dot(20,relleno) #dibujar punto

#Plantilla recta
#def recta(x1, y1, x2, y2, rotar, escalar, tx, ty, color):
def recta(simbolos,identificador,linea):
  p1= obtener_punto(1,identificador,simbolos)
  p2= obtener_punto(2,identificador,simbolos)
  
  x1 = obtener_x(p1,simbolos)
  y1 = obtener_y(p1,simbolos)
  x2 = obtener_x(p2,simbolos)
  y2 = obtener_y(p2,simbolos)  

  rotar = obtener_rotar(identificador, simbolos,linea)
  escalar = obtener_escalar(identificador, simbolos,linea)
  relleno = obtener_color(obtener_relleno(identificador,simbolos,linea))  
  turtle.color(relleno)

  tx = obtener_tx(identificador, simbolos,linea)
  ty = obtener_ty(identificador, simbolos,linea)
  
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

  if rotar != 0:
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
  elif escalar != 0:
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
  else:
    turtle.penup()
    turtle.setposition(x1,y1)
    turtle.pendown()
    turtle.pensize(8)
    turtle.setposition(x2,y2)

#def curva():
def curva(simbolos,identificador,linea):
  p1= obtener_punto(1,identificador,simbolos)
  p2= obtener_punto(2,identificador,simbolos)
  
  x1 = int (obtener_x(p1,simbolos))
  y1 = int (obtener_y(p1,simbolos))
  x2 = obtener_x(p2,simbolos)
  y2 = obtener_y(p2,simbolos)  

  rotar = obtener_rotar(identificador, simbolos,linea)
  escalar = obtener_escalar(identificador, simbolos,linea)
  relleno = obtener_color(obtener_relleno(identificador,simbolos,linea))  
  turtle.color(relleno)

  tx = obtener_tx(identificador, simbolos,linea)
  ty = obtener_ty(identificador, simbolos,linea)
  potencia = obtener_potencia(identificador,simbolos)
  
  #Trasladar recta
  x1 = int(x1*44 + tx*44)
  x2 = int(x2*44 + tx*44)
  y1 = y1*44 + ty*44
  y2 = y2*44 + ty*44  
  turtle.penup()
  for x in range(x1,x2):
  	turtle.goto(x+(44), (x+(44))**potencia)
  	turtle.pendown()

#Plantilla triangulo
#def triangulo(simbolos,p1,p2,p3,rotar,escalar,tx,ty,color):
def triangulo(simbolos,identificador,linea):
  
  p1= obtener_punto(1,identificador,simbolos)
  p2= obtener_punto(2,identificador,simbolos)
  p3= obtener_punto(3,identificador,simbolos)

  x1 = obtener_x(p1,simbolos)
  y1 = obtener_y(p1,simbolos)
  x2 = obtener_x(p2,simbolos)
  y2 = obtener_y(p2,simbolos)
  x3 = obtener_x(p3,simbolos)
  y3 = obtener_y(p3,simbolos)

  tx = obtener_tx(identificador, simbolos,linea)
  ty = obtener_ty(identificador, simbolos,linea)
  
  borde = obtener_color(obtener_borde(identificador,simbolos,linea))
  relleno = obtener_color(obtener_relleno(identificador,simbolos,linea))

  #Trasladar triangulo
  x1 = x1*44 + tx*44
  y1 = y1*44 + ty*44  
  x2 = x2*44 + tx*44
  y2 = y2*44 + ty*44
  x3 = x3*44 + tx*44
  y3 = y3*44 + ty*44

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

  escalar = obtener_escalar(identificador, simbolos,linea)
  #Calcular nuevos puntos para escalar
  if escalar != 0:
    turtle.setposition(incentro_x, incentro_y)
    turtle.setheading(0)
    turtle.lt(a1)
    turtle.forward(d1*escalar)
    x1 = turtle.xcor()
    y1 = turtle.ycor()

    turtle.setposition(incentro_x, incentro_y)
    turtle.setheading(0)
    turtle.lt(a2)
    turtle.forward(d2*escalar)
    x2 = turtle.xcor()
    y2 = turtle.ycor()
   
    turtle.setposition(incentro_x, incentro_y)
    turtle.setheading(0)
    turtle.lt(a3)
    turtle.forward(d3*escalar)
    x3 = turtle.xcor()
    y3 = turtle.ycor()

  rotar = obtener_rotar(identificador, simbolos,linea)
  if rotar != 0: 
    #Calcular nuevos puntos para rotar
    turtle.setposition(incentro_x, incentro_y)
    turtle.setheading(0)
    turtle.lt(a1+rotar)
    turtle.forward(d1)
    x1 = turtle.xcor()
    y1 = turtle.ycor()

    turtle.setposition(incentro_x, incentro_y)
    turtle.setheading(0)
    turtle.lt(a2+rotar)
    turtle.forward(d2)
    x2 = turtle.xcor()
    y2 = turtle.ycor()
   
    turtle.setposition(incentro_x, incentro_y)
    turtle.setheading(0)
    turtle.lt(a3+rotar)
    turtle.forward(d3)
    x3 = turtle.xcor()
    y3 = turtle.ycor()

  #Dibujar triangulo
  turtle.penup()
  turtle.setposition(x1,y1)
  turtle.pendown()
  turtle.color(borde)
  turtle.fillcolor(relleno)
  turtle.begin_fill()
  turtle.pensize(8)
  turtle.setposition(x2,y2)
  turtle.setposition(x3,y3)
  turtle.setposition(x1,y1)
  turtle.end_fill()

#Plantilla cuadrilatero
#def cuadrilatero(simbolos,p1,p2,p3,p4,rotar,escalar,tx,ty,color):
def cuadrilatero(simbolos,identificador,linea):
  p1= obtener_punto(1,identificador,simbolos)
  p2= obtener_punto(2,identificador,simbolos)
  p3= obtener_punto(3,identificador,simbolos)
  p4= obtener_punto(4,identificador,simbolos)

  #Obtener coordenadas
  x1 = obtener_x(p1,simbolos)*44
  y1 = obtener_y(p1,simbolos)*44
  x2 = obtener_x(p2,simbolos)*44
  y2 = obtener_y(p2,simbolos)*44
  x3 = obtener_x(p3,simbolos)*44
  y3 = obtener_y(p3,simbolos)*44
  x4 = obtener_x(p4,simbolos)*44
  y4 = obtener_y(p4,simbolos)*44

  tx = obtener_tx(identificador, simbolos,linea)
  ty = obtener_ty(identificador, simbolos,linea)
  
  borde = obtener_color(obtener_borde(identificador,simbolos,linea))
  relleno = obtener_color(obtener_relleno(identificador,simbolos,linea))

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

  escalar = obtener_escalar(identificador, simbolos,linea)
  #Calcular nuevos puntos para escalar
  if escalar != 0:
    turtle.setposition(punto_medio_x, punto_medio_y)
    turtle.setheading(0)
    turtle.lt(a1)
    turtle.forward(d1*escalar)
    x1 = turtle.xcor()
    y1 = turtle.ycor()

    turtle.setposition(punto_medio_x, punto_medio_y)
    turtle.setheading(0)
    turtle.lt(a2)
    turtle.forward(d2*escalar)
    x2 = turtle.xcor()
    y2 = turtle.ycor()
   
    turtle.setposition(punto_medio_x, punto_medio_y)
    turtle.setheading(0)
    turtle.lt(a3)
    turtle.forward(d3*escalar)
    x3 = turtle.xcor()
    y3 = turtle.ycor()

    turtle.setposition(punto_medio_x, punto_medio_y)
    turtle.setheading(0)
    turtle.lt(a4)
    turtle.forward(d4*escalar)
    x4 = turtle.xcor()
    y4 = turtle.ycor()

  rotar = obtener_rotar(identificador, simbolos,linea)
  if rotar != 0:
    #Calcular nuevos puntos para rotar
    turtle.setposition(punto_medio_x, punto_medio_y)
    turtle.setheading(0)
    turtle.lt(a1+rotar)
    turtle.forward(d1)
    x1 = turtle.xcor()
    y1 = turtle.ycor()

    turtle.setposition(punto_medio_x, punto_medio_y)
    turtle.setheading(0)
    turtle.lt(a2+rotar)
    turtle.forward(d2)
    x2 = turtle.xcor()
    y2 = turtle.ycor()
   
    turtle.setposition(punto_medio_x, punto_medio_y)
    turtle.setheading(0)
    turtle.lt(a3+rotar)
    turtle.forward(d3)
    x3 = turtle.xcor()
    y3 = turtle.ycor()

    turtle.setposition(punto_medio_x, punto_medio_y)
    turtle.setheading(0)
    turtle.lt(a4+rotar)
    turtle.forward(d4)
    x4 = turtle.xcor()
    y4 = turtle.ycor()

  #Dibujar cuadrilatero
  turtle.color(borde)         
  turtle.penup()
  turtle.setposition(x1,y1)
  turtle.pendown()
  turtle.pensize(8)
  turtle.fillcolor(relleno)
  turtle.begin_fill()
  turtle.setposition(x2,y2)
  turtle.setposition(x3,y3)
  turtle.setposition(x4,y4)
  turtle.setposition(x1,y1)
  turtle.end_fill()
  
#def circunferencia(simbolos,radio,centro,escalar,tx,ty,color):
def circunferencia(simbolos,identificador,linea):
  p1= obtener_punto(2,identificador,simbolos)
  radio = obtener_radio(identificador,simbolos)
    
  x1 = obtener_x(p1,simbolos)
  y1 = obtener_y(p1,simbolos)
  
  escalar = obtener_escalar(identificador, simbolos,linea)
  relleno = obtener_color(obtener_relleno(identificador,simbolos,linea))
  borde = obtener_color(obtener_borde(identificador,simbolos,linea))  
  turtle.color(borde)

  tx = obtener_tx(identificador, simbolos,linea)
  ty = obtener_ty(identificador, simbolos,linea)
 
  turtle.pensize(8)
  turtle.penup()

  
  #Trasladar circunferencia
  x1 = x1 + tx*44
  y1 = y1 + ty*44

  turtle.setposition(x1, y1-(radio*44))
  turtle.pendown()
  turtle.circle(radio*44)

  #Escalar circunferencia
  turtle.penup()
  turtle.setposition(x1, y1-(radio*44*escalar))
  turtle.pendown()
  turtle.fillcolor(relleno)
  turtle.begin_fill()
  turtle.circle(radio*44*escalar)
  turtle.end_fill()

#Parabola
def parabola(simbolos,centro):
  x1 = obtener_x(centro,simbolos)*44
  y1 = obtener_y(centro,simbolos)*44
  print "x1=",x1
  print "y1=",y1  
  turtle.color("violet")
  turtle.penup()
  for x in range(-44,44):
    turtle.goto(x+(x1), 0.1*(x)**2+(y1))
    turtle.pendown()

#Elipse
def elipse():
  turtle.color("gray")
  turtle.penup()
  turtle.goto(math.degrees(0.5*math.cos(0))+(44*4), math.degrees(0.8*math.sin(0))-(44*4))
  turtle.pendown()
  turtle.fillcolor("red")
  turtle.begin_fill()  
  for x in range(1,44):
    turtle.goto(math.degrees(0.5*math.cos(x))+(44*4), math.degrees(0.8*math.sin(x))-(44*4))
  turtle.end_fill()  

#Hiperbola
def hiperbola():
  turtle.color("pink")
  turtle.penup()
  for x in range(-2,3):
    turtle.goto(math.degrees(0.5*math.cosh(x)), math.degrees(0.8*math.sinh(x)))
    turtle.pendown()

#Traducir color a Ingles
def obtener_color(color):
  color = color
  if color == "azul" or color == "Azul":
    color = "blue"
  elif color == "rojo" or color == "Rojo":
    color = "red"
  elif color == "naranja" or color == "Naranja":
    color = "orange"
  elif color == "marron" or color == "Marron":
    color = "brown"
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
  for a in simbolos[0]:
    if (a[1]== punto):
      return float(a[3])
  return 0

#Extraer coordenada y de un punto
def obtener_y(punto, simbolos):
  for a in simbolos[0]:
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

def tipo (identificador,simbolos):
  for s in simbolos[0]:
    if (s[1]==identificador):
      return s[2]

def obtener_punto(numero,identificador,simbolos):
  for s in simbolos[0]:
    if (s[1]==identificador):
      if (int(numero) == 1):
        return s[3] 
      elif (int(numero) ==2):
        return s[4]
      elif (int(numero) ==3):
        return s[5]
      elif (int(numero) ==4):
        return s[6]

def obtener_tx(identificador, simbolos,linea):
  for s in simbolos[1]:
    if ((s[0]==identificador)and(linea==s[7])):
      return float(s[3])

def obtener_ty(identificador, simbolos,linea):
  for s in simbolos[1]:
    if ((s[0]==identificador)and(linea==s[7])):
      return float(s[4])

def obtener_borde(identificador, simbolos,linea):
  for s in simbolos[1]:
    if ((s[0]==identificador)and(linea==s[7])):
      return s[5]

def obtener_relleno(identificador, simbolos,linea):
  for s in simbolos[1]:
    if ((s[0]==identificador)and(linea==s[7])):
      return s[6]

def obtener_escalar(identificador, simbolos,linea):
  for s in simbolos[1]:
    if ((s[0]==identificador)and(linea==s[7])):
      return float(s[2])

def obtener_rotar(identificador, simbolos,linea):
  for s in simbolos[1]:
    if ((s[0]==identificador)and(linea==s[7])):
      return float(s[1])

def obtener_potencia(identificador, simbolos):
  for s in simbolos[0]:
    if (s[1]==identificador):
      return float(s[5])

def obtener_radio(identificador, simbolos):
  for s in simbolos[0]:
    if (s[1]==identificador):
      return float(s[3])
