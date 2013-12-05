#! /usr/bin/python
# -*- coding: utf-8 -*-

import ply.lex as lex
import pygtk
import gtk
import os

#http://www.gacetadelinux.com/es/lg/issue79/divakaran.html
class TextViewExample:
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
    t_Identificador = r'[a-z]+[\d]+[\s]'
    t_Propiedad = r'((coordenada)|(extremo)|(vertice)|(semiEje))[\s]'
    t_Delimitador = r'\:'
    t_Fin = r'FINALIZAR'
    t_Accion = r'((Definir)|(Colorear)|(Dibujar)|(Rotar)|(Escalar)|(Trasladar))[\s]'
    t_Reservado = r'((como)|(en)|(de)|(hasta)|(a))[\s]'
    t_Atributo = r'((origen)|(escala)|(centro)|(altura)|(radio)|(x)|(y)|(A)|(B)|(C)|(D))[\s]'
    t_Tipo = r'((Punto)|(Recta)|(Parabola)|(Hiperbola)|(SemiRecta)|(Segmento)|(Curva)|(Circunferencia)|(Cuadrilatero)|(Triangulo)|(Cono)|(Esfera)|(Elipse)|(Cilindro))[\s]'
    t_Unidad = r'((grados)|(unidades)|(veces))[\s]'
    t_Color = r'(([rR]ojo)|([aA]zul)|([aA]marillo)|([vV]erde)|([mM]orado)|([gG]ris)|([nN]egro)|([rR]osado))[\s]'
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
    def compilar(self, data, lexer):
        tabla_id = {}
        lexer.input(data)
        token=open('tokens.cg', 'w')
        while True:
          tok = lexer.token()
          if not tok:
            break
          token.write(str(tok))
          token.write('\n')
          print tok
          #Guardar identificadores en la tabla de simbolos
          tokn = str(tok)
          if tokn.find("Identificador") >= 0:
            separado = tokn.split('\'',3)
            tabla_id[str(separado[1])] = 0
        print "\nElementos de la Tabla de Simbolos"
        for key in tabla_id.keys():
          print key  
        token.close()

    def abrir(self, Button, textbuffer):
        textbuffer = textbuffer
        dialog = gtk.FileChooserDialog("Abrir archivo",None,
gtk.FILE_CHOOSER_ACTION_OPEN,(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
gtk.STOCK_OPEN, gtk.RESPONSE_OK))
        dialog.set_default_response(gtk.RESPONSE_OK)

        filter = gtk.FileFilter()
        filter.set_name("Archivos CG")
        dialog.set_filename('ejemplos/*')
        filter.add_pattern("*.CG")
        dialog.add_filter(filter)

        filter = gtk.FileFilter()
        filter.set_name("Todos los archivos")
        filter.add_pattern("*")
        dialog.add_filter(filter)

        response = dialog.run()
        if response == gtk.RESPONSE_OK:
            try:
                infiles=open(dialog.get_filename(),'r')
                if infiles:
                  string = infiles.read()
                  infiles.close()
                  textbuffer.set_text(string)
            except IOError :
                print "El fichero no existe."
            infiles.close()
        elif response == gtk.RESPONSE_CANCEL:
            print "No hay elementos seleccionados"
        dialog.destroy()

    def close_application(self, widget):
        gtk.main_quit()

    lexer = lex.lex()

    def mostrarresultados(self, textbuffer):
        textbuffer = textbuffer
        n = os.system('ls *.cg | wc -l')
        if n > 1:
            resultado = ['errorLexico.cg']
        else:
            resultado = ['tokens.cg']

        for codigo in resultado:
            f = open(codigo, 'r')
            if f:
              string = f.read()
              f.close()
              textbuffer.set_text(string)

    def ejecutar(self, Button, textbuffer):
        textbuffer = textbuffer
        texto = textbuffer.get_text(textbuffer.get_start_iter(), textbuffer.get_end_iter(), True)
        if texto:
            self.lexer.input(texto)
            self.compilar(texto, self.lexer)
        self.mostrarresultados(textbuffer)

    def __init__(self):

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
    #ejemplo = ['ejemplos/cilindro.CG']

        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_resizable(True)  
        window.connect("destroy", self.close_application)
        window.set_title("Compilador Geométrico")
        window.set_size_request(800, 700)
        window.set_border_width(5)

        box1 = gtk.VBox(False, 0)
        window.add(box1)
        box1.show()

        box2 = gtk.VBox(False, 10)
        box2.set_border_width(10)
        box1.pack_start(box2, True, True, 0)
        box2.show()

        sw = gtk.ScrolledWindow()
        sw.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        textview = gtk.TextView()
        self.textbuffer = textview.get_buffer()
        sw.add(textview)
        sw.show()
        textview.show()

        box2.pack_start(sw)

        hbox = gtk.HButtonBox()
        box2.pack_start(hbox, False, False, 0)
        hbox.show()

        vbox = gtk.VBox()
        vbox.show()
        hbox.pack_start(vbox, False, False, 0)

        separator = gtk.HSeparator()
        box1.pack_start(separator, False, True, 0)
        separator.show()

        button2 = gtk.Button("Abrir...")
        button2.connect("clicked", self.abrir, self.textbuffer)
        box2.pack_start(button2, True, True, 0)

        box2 = gtk.HBox(False, 10)
        box2.set_border_width(10)
        box1.pack_start(box2, False, True, 0)
        box2.show()

        button2 = gtk.Button("Abrir...")
        button2.connect("clicked", self.abrir, self.textbuffer)
        box2.pack_start(button2, False, False, 0)
        button2.show()

        button1 = gtk.Button("Compilar")
        button1.connect("clicked", self.ejecutar, self.textbuffer)
        box2.pack_start(button1, False, False, 0)
        button1.set_flags(gtk.CAN_DEFAULT)
        button1.grab_default()
        button1.show()

        button = gtk.Button("Cerrar")
        button.connect("clicked", self.close_application)
        box2.pack_start(button, False, False, 0)
        button.set_flags(gtk.CAN_DEFAULT)
        button.grab_default()
        button.show()

        window.show()

def main():
    gtk.main()
    return 0       

if __name__ == "__main__":
    TextViewExample()
    main()

