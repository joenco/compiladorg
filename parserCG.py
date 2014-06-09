import ply.yacc as yacc
import lexico
from lexico import tokens
import sys

VERBOSE = 1

def p_programa(p):
	'programa : Inicio lista_sentencia Fin'
	pass

def p_lista_sentencia_1(p):
	'lista_sentencia : lista_sentencia sentencia'
	pass

def p_lista_sentencia_2(p):
	'lista_sentencia : sentencia'
	pass

def p_sentencia(p):
	'''sentencia : definicion 
				  | asignacion
                                  | accion '''
	pass

def p_definicion(p):
	'definicion : Accion Identificador Reservado Tipo Delimitador'
	pass

def p_definicion_error(p):
	'definicion : Accion error Delimitador'
	print "Error de Sintaxis"

def p_asignacion_1(p):
	'asignacion : Reservado Propiedad Atributo Reservado Identificador Asignacion Valor Delimitador'
	pass

def p_asignacion_1_error(p):
	'asignacion : Reservado error Delimitador'
	print "Error de Sintaxis"

def p_asignacion_2(p):
	'asignacion : Reservado Propiedad Atributo Reservado Identificador Asignacion Identificador Delimitador'
	pass

def p_asignacion_3(p):
	'asignacion : Reservado Atributo Reservado Identificador Asignacion Valor Delimitador'
	pass

def p_asignacion_4(p):
	'asignacion : Reservado Atributo Reservado Identificador Asignacion Identificador Delimitador'
	pass

def p_asignacion_5(p):
	'asignacion : Reservado Propiedad Reservado Identificador Asignacion Valor Delimitador'
	pass

def p_accion(p):
	'''accion : rotacion 
				  | traslacion
                                  | coloreado 
                                  | escalado
                                  | dibujado'''
	pass

def p_rotacion(p):
	'rotacion : Accion Identificador Reservado Valor Unidad Delimitador'
	pass

def p_traslacion(p):
	'traslacion : Accion Reservado Atributo Identificador Reservado Valor Unidad Delimitador'
	pass

def p_coloreado(p):
	'coloreado : Accion Atributo Reservado Identificador Reservado Color Delimitador'
	pass

def p_escalado(p):
	'escalado : Accion Identificador Valor Unidad Delimitador'
	pass

def p_dibujado(p):
	'dibujado : Accion Identificador Delimitador'
	pass

def p_error(p):
	
	if VERBOSE:
		if p is not None:
                        error=open('.errorSintaxis.cg', 'a')
          	        error.write(str(p.lexer.lineno)+":"+str(p.value)+":")
          		error.write('\n')
        		error.close()
		
		else:
                        error=open('.errorSintaxis.cg', 'a')
          	        error.write(str(lexico.lexer.lineno)+":"+"fin"+":")
          		error.write('\n')
        		error.close()
			print "Error de sintaxis en la linea: " + str(lexico.lexer.lineno)
	else:
		raise Exception('syntax', 'error')
		
def parse(data):
    lexico.lexer.lineno = 1    
    parser.parse(data, tracking=True)
    

parser = yacc.yacc()

if __name__ == '__main__':

	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'ejemplos/cilindro.CG'

	f = open(fin, 'r')
	data = f.read()
	print data
	parser.parse(data, tracking=True)
	

