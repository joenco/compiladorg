#! /usr/bin/python
# -*- coding: utf-8 -*-

import ply.lex as lex
import pygtk
import gtk
import os
import tokens

# Nuevo archivo
def new(self, textbuffer, window, vistas):
    textbuffer = textbuffer
    window = window
    vistas = vistas

    #pendiente por resolver
    #if textbuffer.get_modified() == True:
        #changeverify(self, textbuffer, window)

    textbuffer.delete(textbuffer.get_start_iter(), textbuffer.get_end_iter())
    textbuffer.set_modified(False)
    window.set_title("Archivo nuevo sin guardar")
    try:
        vistas.remove_page(1)
    except IOError :
        print "No hay pestañas para eliminar"

#Abrir archivo
def openfile(self, textbuffer, window):
    textbuffer = textbuffer
    window = window

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
        textbuffer.set_modified(False)
        infiles.close()
    elif response == gtk.RESPONSE_CANCEL:
        print "No hay elementos seleccionados"

    window.set_title(str(dialog.get_filename()))
    dialog.destroy()

def savefile(self, textbuffer, window):
        textbuffer = textbuffer
        window = window
        filename = window.get_title()

        if filename != "Archivo nuevo sin guardar":
            try:
                texto=open(filename, 'w')
                texto.write(textbuffer.get_text(textbuffer.get_start_iter(), textbuffer.get_end_iter(), True)+"\n")
            except IOError :
                print "El fichero no existe."
            textbuffer.set_modified(False)
            texto.close()
        else:
            saveasfile(self, textbuffer, window)

def saveasfile(self, textbuffer, window):
        textbuffer = textbuffer
        window = window

        dialog = gtk.FileChooserDialog("Guardar archivo",None,
gtk.FILE_CHOOSER_ACTION_SAVE,(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
gtk.STOCK_SAVE, gtk.RESPONSE_OK))
        dialog.set_default_response(gtk.RESPONSE_OK)
        response = dialog.run()
        if response == gtk.RESPONSE_OK:
            try:
                texto = open(dialog.get_filename(), 'w')
                texto.write(textbuffer.get_text(textbuffer.get_start_iter(), textbuffer.get_end_iter(), True)+"\n")
            except IOError :
                print "El fichero no existe."
            textbuffer.set_modified(False)
            texto.close()
        elif response == gtk.RESPONSE_CANCEL:
            print "No hay elementos seleccionados"

        window.set_title(str(dialog.get_filename()))
        dialog.destroy()

#cerrar la aplicación
def close(self, textbuffer, window):
        textbuffer = textbuffer
        if textbuffer.get_modified() == True:
            changeverify(self, textbuffer, window)
        gtk.main_quit()

#Verificar modificaciones
def changeverify(self, textbuffer, window):
        textbuffer = textbuffer
        window = window
        dialog = gtk.Dialog("Aviso", None, 0, (gtk.STOCK_NO, gtk.RESPONSE_CANCEL, gtk.STOCK_YES, gtk.RESPONSE_OK))
        dialog.set_default_response(gtk.RESPONSE_OK)
        label = gtk.Label('Tiene cambios sin guardar, desea guardar los cambios?')
        dialog.vbox.pack_start(label, True, True, 0)
        label.show()
        response = dialog.run()
        if response == gtk.RESPONSE_OK:
                return savefile(self, textbuffer, window)
        elif response == gtk.RESPONSE_CANCEL:
                return False
        dialog.destroy()

#Buscar linea
def findline(self, textbuffer):
        textbuffer = textbuffer
        dialog = gtk.Dialog("Buscar Linéa", None, 0, (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL, gtk.STOCK_FIND, gtk.RESPONSE_OK))
        dialog.set_default_response(gtk.RESPONSE_OK)
        hbox = gtk.HBox(False, 0)
        label = gtk.Label('Nro de linéa: ')
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
                moveline(self, n_linea, textbuffer)
            except IOError :
                print "no es un parámetro válido"
        elif response == gtk.RESPONSE_CANCEL:
            print "No hay elementos seleccionados"
        dialog.destroy()

#Mover el cursor a una linea determinada
def moveline(self, linea, textbuffer):
        linea = linea
        textbuffer = textbuffer
        #iter = self.textbuffer.get_iter_at_offset(linea*2-1)
        iter = textbuffer.get_iter_at_line(linea-1)
        textbuffer.place_cursor(iter)

#resultados
def result(self, textbuffer, vistas, sw1, statusbar, context_id):
        textbuffer = textbuffer
        vistas = vistas
        sw1 = sw1
        statusbar = statusbar
        context_id = context_id

        completo = ""
        posicion = -1
        nolinea = -1
        
        #textbuffer = textbuffer
        #textbuffer1 = textbuffer1
        textbuffer.delete(textbuffer.get_start_iter(), textbuffer.get_end_iter())
        #textbuffer1.delete(textbuffer1.get_start_iter(), textbuffer1.get_end_iter())

        resultado1 = ['.errorLexico.cg']
        resultado2 = ['.tokens.cg']
        label = gtk.Label()
        n_error = 0
        
        #Tratamiento de errores
        try:
          f = open (".errorLexico.cg",'r')
          errores=open('.erroresLexico.cg', 'a')
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
            f = open(".erroresLexico.cg", 'r')
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
            statusbar.push(context_id, label.get_text())
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
            vistas.remove_page(1)
        except IOError :
            print "No hay pestañas para eliminar"
        vistas.append_page(sw1, label)
        vistas.next_page()

def Text(self, textbuffer):
        textbuffer = textbuffer

        self.inicio = textbuffer.get_start_iter()
        self.fin = textbuffer.get_end_iter()
        texto = textbuffer.get_text(self.inicio, self.fin, True)

        return texto

def ejecute(self, textbuffer, textbuffer1, vistas, sw1, statusbar, context_id):
        textbuffer = textbuffer
        textbuffer1 = textbuffer1
        vistas = vistas
        sw1 = sw1
        statusbar = statusbar
        context_id = context_id
        
        os.system('rm .*.cg')
        os.system('clear')
        texto = Text(self, textbuffer)
        if texto:
            tokens.lexico(texto)
        result(self, textbuffer1, vistas, sw1, statusbar, context_id)

#acerca de
def about(self):
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
        aboutdialog.connect("response", on_close)
        aboutdialog.show()

# cerrar la ventana de acerca
def on_close(self):
        action.destroy()
