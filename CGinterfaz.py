#! /usr/bin/python
# -*- coding: utf-8 -*-

import ply.lex as lex
import pygtk
import gtk
import os

#http://www.gacetadelinux.com/es/lg/issue79/divakaran.html
class Interfaz:
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
          #print "Carácter ilegal: '%s'" %  t.value[0] + " en la linea " + str(t.lineno)
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
    def compilar(self, data, lexer):
        tabla_id = {}
        lexer.lineno = 1
        lexer.input(data)
        token=open('tokens.cg', 'w')
        while True:
          tok = lexer.token()
          if not tok:
            print 
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

    def nuevo(self, callback_action, widget):
        self.textbuffer.delete(self.textbuffer.get_start_iter(), self.textbuffer.get_end_iter())
        self.textbuffer.set_modified(False)
        self.filename = 'None'
        self.window.set_title("Archivo nuevo sin guardar | Compilador Geométrico")
        try:
            self.vistas.remove_page(1)
        except IOError :
            print "No hay pestañas para eliminar"

    def abrir(self, callback_action, widget):
        #textbuffer = textbuffer
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
                  self.textbuffer.set_text(string)
            except IOError :
                print "El fichero no existe."
            self.textbuffer.set_modified(False)
            infiles.close()
        elif response == gtk.RESPONSE_CANCEL:
            print "No hay elementos seleccionados"

        self.window.set_title(str(dialog.get_filename())+" | Compilador Geométrico")
        self.filename = dialog.get_filename()
        dialog.destroy()

    def guardar(self,widget,data=None):
        if self.filename != 'None':
            try:
                texto=open(self.filename, 'w')
                texto.write(self.textbuffer.get_text(self.textbuffer.get_start_iter(), self.textbuffer.get_end_iter(), True)+"\n")
            except IOError :
                print "El fichero no existe."
            self.textbuffer.set_modified(False)
            texto.close()
        else:
            self.guardar_como(self,widget)

    def guardar_como(self,widget, data=None):
        dialog = gtk.FileChooserDialog("Guardar archivo",None,
gtk.FILE_CHOOSER_ACTION_SAVE,(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
gtk.STOCK_SAVE, gtk.RESPONSE_OK))
        dialog.set_default_response(gtk.RESPONSE_OK)
        response = dialog.run()
        if response == gtk.RESPONSE_OK:
            try:
                texto = open(dialog.get_filename(), 'w')
                texto.write(self.textbuffer.get_text(self.textbuffer.get_start_iter(), self.textbuffer.get_end_iter(), True)+"\n")
            except IOError :
                print "El fichero no existe."
            self.textbuffer.set_modified(False)
            texto.close()
        elif response == gtk.RESPONSE_CANCEL:
            print "No hay elementos seleccionados"
        self.filename = dialog.get_filename()
        self.window.set_title(str(dialog.get_filename())+" | Compilador Geométrico")
        dialog.destroy()

    def buscarlinea(self, callback_action, widget, data=None):
        dialog = gtk.Dialog("Buscar Linéa", None, 0, (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL, gtk.STOCK_FIND, gtk.RESPONSE_OK))
        dialog.set_default_response(gtk.RESPONSE_OK)
        hbox = gtk.HBox(False, 0)
        label = gtk.Label('Nro de linéa: ')
        n = self.textbuffer.get_line_count()
        entry = gtk.Entry()
        hbox.pack_start(label, False, False, 0)
        hbox.pack_start(entry, False, False, 0)
        dialog.vbox.pack_start(hbox, True, True, 0)
        label.show()
        entry.show()
        hbox.show()
        response = dialog.run()
        if response == gtk.RESPONSE_OK:
            try:
                n_linea = int(entry.get_text())
                self.mover(n_linea)
            except IOError :
                print "no es un parámetro válido"
        elif response == gtk.RESPONSE_CANCEL:
            print "No hay elementos seleccionados"
        dialog.destroy()

    #Mover el cursor a una linea determinada
    def mover(self, linea):
        linea = linea
        #iter = self.textbuffer.get_iter_at_offset(linea*2-1)
        iter = self.textbuffer.get_iter_at_line(linea-1)
        self.textbuffer.place_cursor(iter)

    def acerca(self, callback_action, widget, data=None):
        aboutdialog = gtk.AboutDialog()
        authors = ["Jorge Ortega", "Jesús Pérez"]
        #documenters = ["GNOME Documentation Team"]
        aboutdialog.set_program_name("CG: Compilador Geométrico")
        aboutdialog.set_copyright("GPL 3.0")
        aboutdialog.set_authors(authors)
        #aboutdialog.set_documenters(documenters)
        aboutdialog.set_website("http://code.google.com/p/compiladorg/")
        aboutdialog.set_website_label("CG - Compilador Geométrico Website")
        aboutdialog.set_title("Acerca de..")
        aboutdialog.connect("response", self.on_close)
        aboutdialog.show()

    # cerrar la ventana de acerca
    def on_close(self, action, parameter):
        action.destroy()

    #cerrar la aplicación
    def cerrar(self, callback_action, widget):
        if self.textbuffer.get_modified() == True:
            self.verificarcambios()
        gtk.main_quit()
        os.system('rm *.cg')

    def verificarcambios(self):
        dialog = gtk.Dialog("Aviso", None, 0, (gtk.STOCK_NO, gtk.RESPONSE_CANCEL, gtk.STOCK_YES, gtk.RESPONSE_OK))
        dialog.set_default_response(gtk.RESPONSE_OK)
        label = gtk.Label('Tiene cambios sin guardar, desea guardar los cambios?')
        dialog.vbox.pack_start(label, True, True, 0)
        label.show()
        response = dialog.run()
        if response == gtk.RESPONSE_OK:
                return self.guardar(self)
        elif response == gtk.RESPONSE_CANCEL:
                return False
        dialog.destroy()

    lexer = lex.lex()

    def get_main_menu(self):
        accel_group = gtk.AccelGroup()
        item_factory = gtk.ItemFactory(gtk.MenuBar, "<main>", accel_group)
        item_factory.create_items(self.menu_items)

        self.window.add_accel_group(accel_group)

        self.item_factory = item_factory

        return item_factory.get_widget("<main>")

    def mostrarresultados(self, textbuffer):
        completo = ""
        posicion = -1
        nolinea = -1
        
        textbuffer = textbuffer
        #textbuffer1 = textbuffer1
        textbuffer.delete(textbuffer.get_start_iter(), textbuffer.get_end_iter())
        #textbuffer1.delete(textbuffer1.get_start_iter(), textbuffer1.get_end_iter())

        resultado1 = ['errorLexico.cg']
        resultado2 = ['tokens.cg']
        label = gtk.Label()
        n_error = 0
        
        #Tratamiento de errores
        try:
          f = open ("errorLexico.cg",'r')
          errores=open('erroresLexico.cg', 'a')
          for line in f.readlines():
            separados = line.split(':',3)
            if posicion != -1:
              if (posicion + 1) == int(separados[2]):
                completo += str(separados[0])
              else:
                print "Error encontrado: ",completo
                print "Linea: ",nolinea 
                errores.write("Error: %s" % completo + " en la linea numero " + str(nolinea))
                errores.write('\n')
                completo = ""
                completo += str(separados[0]) 
              posicion = int(separados[2])
              nolinea = int(separados[1])
            else:
              posicion = int(separados[2])
              nolinea = int(separados[1])
              completo += str(separados[0])
          if completo != "":
            print "Error encontrado: ",completo
            print "Linea: ",nolinea 
            errores.write("Error: %s" % completo + " en la linea numero " + str(nolinea))
            errores.write('\n')
            completo = ""
          errores.close()
          f.close()
        except IOError :
          print "El Analizador Lexico no encontro errores"    
         
        try:
            #for codigo in resultado1:
            f = open("erroresLexico.cg", 'r')
            if f:
              string = f.read()
              f.close()
              textbuffer.set_text(string)

            n_error = textbuffer.get_line_count()-1
            if (n_error == 1):
              label.set_text(str(n_error)+" Error")
            else: 
              label.set_text(str(n_error)+" Errores")
            label.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse('red'))
            self.statusbar.push(self.context_id, label.get_text())
            os.system('rm tokens.cg')
        except IOError :
            for codigo in resultado2:
              f = open(codigo, 'r')
              if f:
                string = f.read()
                f.close()
                textbuffer.set_text(string)
            label.set_text("Tokens")
            label.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse('blue'))

        try:
            self.vistas.remove_page(1)
        except IOError :
            print "No hay pestañas para eliminar"
        self.vistas.append_page(self.sw1, label)
        self.vistas.next_page()

    def Texto(self, textbuffer):
        textbuffer = textbuffer

        self.inicio = textbuffer.get_start_iter()
        self.fin = textbuffer.get_end_iter()
        texto = textbuffer.get_text(self.inicio, self.fin, True)

        return texto

    def ejecutar(self, callback_action, widget):
        os.system('rm *.cg')
        os.system('clear')
        texto = self.Texto(self.textbuffer)
        if texto:
            self.lexer.input(texto)
            self.compilar(texto, self.lexer)
        self.mostrarresultados(self.textbuffer1)

    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_resizable(True)  
        self.window.connect("destroy", self.cerrar)
        self.window.set_title("Archivo nuevo sin guardar | Compilador Geométrico")
        self.window.set_size_request(800, 700)
        self.window.set_border_width(5)

        self.vistas = gtk.Notebook()
        self.vistas.set_tab_pos(gtk.POS_RIGHT)

        box1 = gtk.VBox(False, 0)
        self.window.add(box1)
        self.filename = 'None'
        box1.show()

        box2 = gtk.VBox(False, 10)
        box2.set_border_width(10)
        box1.pack_start(box2, True, True, 0)
        box2.show()

        sw = gtk.ScrolledWindow()
        sw.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        self.textview = gtk.TextView()
        self.textbuffer = self.textview.get_buffer()
        sw.add(self.textview)
        sw.show()
        self.textview.show()

        label = gtk.Label("Fuente")
        label.show()
        self.vistas.append_page(sw, label)

        self.sw1 = gtk.ScrolledWindow()
        self.sw1.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        textview1 = gtk.TextView()
        textview1.set_editable(False)
        self.textbuffer1 = textview1.get_buffer()
        self.sw1.add(textview1)
        self.sw1.show()
        textview1.show()

        # creamos una barra de estado
        self.statusbar = gtk.Statusbar()
        self.context_id = self.statusbar.get_context_id("")
        self.statusbar.push(self.context_id, " ")

        self.menu_items = (
            ( "/_Archivo",         None,         None, 0, "<Branch>" ),
            ( "/Archivo/_Nuevo",     "<control>N", self.nuevo, 0, None ),
            ( "/Archivo/_Abrir...",    "<control>O", self.abrir, 0, None ),
            ( "/Archivo/_Guardar",    "<control>G", self.guardar, 0, None ),
            ( "/Archivo/Guardar _como",    "<control>S", self.guardar_como, 0, None ),
            ( "/Archivo/sep1",     None,         None, 0, "<Separator>" ),
            ( "/Archivo/_Salir",     "<control>Q", self.cerrar, 0, None ),
            ( "/_Ir",      None,         None, 0, "<Branch>" ),
            ( "/Ir/_Buscar linéa",     "<control>b", self.buscarlinea, 0, None ),
            ( "/_Herramientas",      None,         None, 0, "<Branch>" ),
            ( "/Herramientas/Analizador",     None, None, 0, "<Branch>" ),
            ( "/Herramientas/Analizador/Léxico linéa",     "<control>l", self.ejecutar, 0, None ),
            ( "/Herramientas/Analizador/Sintáctico",     None, None, 0, None ),
            ( "/Herramientas/Analizador/Semántico",     None, None, 0, None ),
            ( "/Herramientas/Dibujar",     None, None, 0, "<Branch>" ),
            ( "/Ay_uda",         None,         None, 0, "<LastBranch>" ),
            ( "/Ayuda/Acerca de ...",     "<control>h", self.acerca, 0, None ),
            )

        menubar = self.get_main_menu()

        box2.pack_start(menubar, False, False, 0)
        menubar.show()

        separator = gtk.HSeparator()
        box2.pack_start(separator, False, True, 0)
        separator.show()

        box2.pack_start(self.vistas)
        box2.pack_start(self.statusbar, False, False, 0)
        self.vistas.show()
        self.statusbar.show()
        self.show_tabs = True
        self.show_border = True

        self.window.show()

def main():
    gtk.main()
    return 0       

if __name__ == "__main__":
    Interfaz()
    main()

