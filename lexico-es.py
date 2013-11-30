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
   'Identificador',
   'Asignacion',
   'Propiedad',
   'Signo',
   'Final',
   'Fin',
   'Accion',
   'Reservado',
   'Atributo',
   'Tipo',
   'Color',
   'Valor'
)

# Declaraciones regulares de reglas para los tokens.
t_Inicio = r'INICIAR'
t_Identificador = r'[a-z]+[\d]+'
t_Asignacion = r'asignar'
t_Propiedad = r'coordenada'
t_Signo = r'(\+)|(\-)'
t_Final = r'\:'
t_Fin = r'FINALIZAR'
t_Accion = r'(Definir)|(Colorear)|(Dibujar)|(Rotar)|(MoverX)|(MoverY)|(MoverZ)|(Escalar)|(Trasladar)[\s]'
t_Reservado = r'(como)|(en)|(de)|(hasta)|(repetir)|(veces)|(grados)[\s]'
t_Atributo = r'(alto)|(ancho)|(largo)|(base)|(radio)|(x)|(y)[\s]'
t_Tipo = r'(Punto)|(Recta)|(SemiRecta)|(Segmento)|(Curva)|(Circulo)|(Cuadrado)|(Rectangulo)|(Triangulo)|(Cono)|(Esfera)|(Elipse)'
t_Color = r'([rR]ojo)|([aA]zul)|([aA]marillo)|([vV]erde)|([mM]orado)|([gG]ris)|([nN]egro)'
t_Valor = r'[0-9]{1,}(\.[0-9]{1,})?'

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

    ejemplo = ['ejemplos/punto.CG']
    #ejemplo = ['ejemplos/punto.CG']
    for codigo in ejemplo:
      f = open(codigo, 'r')
      data = f.read()

      # Build lexer and try on
      lexer.input(data)
      test(data, lexer)
