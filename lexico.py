#! /usr/bin/python
# -*- coding: utf-8 -*-

import ply.lex as lex
import os

#http://www.gacetadelinux.com/es/lg/issue79/divakaran.html
os.system('rm .*.cg')
os.system('clear')
# Lista de nombres de Token. Esto es obligatorio.
tokens = (
   'Identificador',
   'Asignacion',
   'Propiedad',
   'Delimitador',
   'Accion',
   'Reservado',
   'Atributo',
   'Tipo',
   'Unidad',
   'Color',
   'Inicio',
   'Fin',
   'Valor'
)

# Declaraciones regulares de reglas para los tokens.
t_Identificador = r'[a-z]+[\d]+[\s]'
t_Asignacion = r'(asignar)[\s]'
t_Propiedad = r'((coordenada)|(extremo)|(vertice)|(semiEje))[\s]'
t_Delimitador = r'\:'
t_Accion = r'((Definir)|(Colorear)|(Dibujar)|(Rotar)|(Escalar)|(Trasladar))[\s]'
t_Reservado = r'((como)|(en)|(de)|(hasta)|(a))[\s]'
t_Atributo = r'((origen)|(escala)|(centro)|(altura)|(radio)|(x)|(y)|(A)|(B)|(C)|(D))[\s]'
t_Tipo = r'((Punto)|(Recta)|(Parabola)|(Hiperbola)|(SemiRecta)|(Segmento)|(Curva)|(Circunferencia)|(Cuadrilatero)|(Triangulo)|(Cono)|(Esfera)|(Elipse)|(Cilindro))[\s]'
t_Unidad = r'((grados)|(unidades)|(veces))[\s]'
t_Color = r'(([rR]ojo)|([aA]zul)|([aA]marillo)|([vV]erde)|([mM]orado)|([gG]ris)|([nN]egro)|([rR]osado))[\s]'
t_Inicio = r'INICIAR'
t_Fin = r'FINALIZAR'
t_Valor = r'[\-]?[0-9]{1,}(\.[0-9]{1,})?[\s]'

def t_comentarios(t):
    r'\#\#(.|\n)*?\#\#'
    t.lexer.lineno += t.value.count('\n')

def t_comentariolinea(t):
    r'\#(.)*?\n'
    t.lexer.lineno += 1

# Una cadena conteniendo carácteres ignorados (espacios y tabulación).
t_ignore  = ' \t'

# Una regla para manejar errores.
def t_error(t):
        error=open('.errorLexico.cg', 'a')
        if t.value!=True:
          print "Carácter ilegal: '%s'" %  t.value[0] + " en la linea " + str(t.lineno)
          error.write(t.value[0] + ":" + str(t.lineno) + ":" + str(t.lexpos))
          error.write('\n')
        error.close()
        t.lexer.skip(1)

# Definir una regla, así podemos localizar los números de líneas.
def t_newline(t):
    r'\n'
    t.lexer.lineno += 1
    #t.lineno += len(t.value)

# Construir el analizador léxico
lex.lex()

# Obtener la entrada
def lexico(data):
    tabla_id = {}
    lexer.input(data)
    lexer.lineno = 1
    token=open('.tokens.cg', 'w')
    while True:
      tok = lexer.token()
      if not tok:
        break
      token.write(str(tok))
      token.write('\n')
      print tok
    token.close()

lexer = lex.lex()

# lexico 
if __name__ == '__main__':

    # lexico
    
    #ejemplo = ['ejemplos/esfera.CG']
    #ejemplo = ['ejemplos/cilindro.CG']  
    #ejemplo = ['ejemplos/cono.CG']
    #ejemplo = ['ejemplos/elipse.CG']
    #ejemplo = ['ejemplos/hiperbola.CG']
    #ejemplo = ['ejemplos/parabola.CG']
    #ejemplo = ['ejemplos/circunferencia.CG']
    #ejemplo = ['ejemplos/cuadrilatero.CG']
    #ejemplo = ['ejemplos/triangulo.CG']    
    #ejemplo = ['ejemplos/recta.CG']
    ejemplo = ['ejemplos/cilindro.CG']
    for codigo in ejemplo:
      f = open(codigo, 'r')
      data = f.read()

      # Build lexer and try on
      lexer.input(data)
      lexico(data)
