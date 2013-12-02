#! /usr/bin/python
# -*- coding: utf-8 -*-

import ply.lex as lex
import os

#http://www.gacetadelinux.com/es/lg/issue79/divakaran.html
os.system('rm *.cg')
os.system('clear')
# Lista de nombres de Token. Esto es obligatorio.
tokens = (
   'Inicio',
   'Asignacion',
   'Identificador',
   'Propiedad',
   'Delimitador',
   'Fin',
   'Accion',
   'Reservado',
   'Atributo',
   'Tipo',
   'Unidad',
   'Color',
   'Valor'
)

# Declaraciones regulares de reglas para los tokens.
t_Inicio = r'INICIAR'
t_Asignacion = r'(asignar)[\s]'
t_Identificador = r'[a-zA-Z][a-z]+[_]?[\d]*'
t_Propiedad = r'(coordenada)|(extremo)|(vertice)|(semiEje)'
t_Delimitador = r'\:'
t_Fin = r'FINALIZAR'
t_Accion = r'((Definir)|(Colorear)|(Dibujar)|(Rotar)|(Escalar)|(Trasladar))[\s]'
t_Reservado = r'((como)|(en)|(de)|(hasta)|(a))[\s]'
t_Atributo = r'((origen)|(escala)|(centro)|(altura)|(radio)|(x)|(y)|(A)|(B)|(C)|(D))[\s]'
t_Tipo = r'((Punto)|(Recta)|(Parabola)|(Hiperbola)|(SemiRecta)|(Segmento)|(Curva)|(Circunferencia)|(Cuadrilatero)|(Triangulo)|(Cono)|(Esfera)|(Elipse)|(Cilindro))[_][^\d]'
t_Unidad = r'(grados)|(unidades)|(veces)'
t_Color = r'([rR]ojo)|([aA]zul)|([aA]marillo)|([vV]erde)|([mM]orado)|([gG]ris)|([nN]egro)|([rR]osado)'
t_Valor = r'[\-]?[0-9]{1,}(\.[0-9]{1,})?'

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
    error=open('errorLexico.cg', 'a')
    if t.value!=True:
      print "Carácter ilegal: '%s'" %  t.value[0] + " en la linea " + str(t.lineno)
      error.write("Carácter ilegal: '%s'" %  t.value[0] + " en la linea " + str(t.lineno))
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
def test(data, lexer):
    lexer.input(data)
    token=open('tokens.cg', 'w')
    while True:
      tok = lexer.token()
      if not tok:
        break
      token.write(str(tok))
      token.write('\n')
      print tok
    token.close()

lexer = lex.lex()

# Test 
if __name__ == '__main__':

    # Test
    
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
    ejemplo = ['ejemplos/punto.CG']
    for codigo in ejemplo:
      f = open(codigo, 'r')
      data = f.read()

      # Build lexer and try on
      lexer.input(data)
      test(data, lexer)
