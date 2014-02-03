#! /usr/bin/python
# -*- coding: utf-8 -*-

import ply.lex as lex
import pygtk
import gtk
import os
import lexico

#abrir pestañas para los nuevos archivos
def openfiles(self, sw, textbuffer, vistas, filename):
        sw=sw
        textbuffer = textbuffer
        vistas = vistas
        filename = filename
        n= nfiles(self, 'None', 0)

        if filename!='Nuevo':
            infiles=open(filename,'r')
            if infiles:
              string = infiles.read()
              infiles.close()
              textbuffer.set_text(string)
        else:
            filename='Codigo fuente '+str(n+1)
        label = gtk.Label(filename)
        label.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse('blue'))
        vistas.append_page(sw, label)
        vistas.next_page()

#buscamos el nombre del archivo
def namefiles(self, page):
    page = page

    file = ['.archivo'+str(page)+'.dat']
    for line in file:
      f = open(line, 'r')
      filename = f.read()
      f.close()

    return filename

#cambia los valores del archivo .n.dat
def nfiles(self, filename, o):
    filename = filename
    o = o

    file=['.n.dat']
    for line in file:
        f = open(line, 'r')
        n= int(f.read())
        f.close()

    if o==0:
        return n
    elif o==1:
        f0=open('.n.dat', 'w')
        f1=open('.archivo'+str(n+1)+'.dat', 'a')
        f0.write(str(n+1))
        f1.write(filename)
        f0.close()
        f1.close()
    elif o==2:
        f0=open('.n.dat', 'w')
        f0.write(str(n-1))
        f0.close()
    else:
        f1=open('.archivo0.dat', 'w')
        f1.write(filename)
        f1.close()
        

# Nuevo archivo
def new(self, sw, textbuffer, vistas):
    sw = sw
    textbuffer = textbuffer
    vistas = vistas
    n= nfiles(self, '0', 0)

    if n>0 or textbuffer[0].get_modified() == True:
        openfiles(self, sw[n+1], textbuffer[n+1], vistas, 'Nuevo')
        nfiles(self, 'nuevo', 1)

#Abrir archivo
def openfile(self, sw, textbuffer, vistas):
    sw = sw
    textbuffer = textbuffer
    vistas=vistas
    
    page = vistas.get_current_page()
    n = nfiles(self, 'None', 0)

    dialog = gtk.FileChooserDialog("Abrir archivo",None,
gtk.FILE_CHOOSER_ACTION_OPEN,(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
gtk.STOCK_OPEN, gtk.RESPONSE_OK))
    dialog.set_default_response(gtk.RESPONSE_OK)

    filter = gtk.FileFilter()
    filter.set_name("Archivos CG")
    dialog.set_filename('ejemplos/*')
    filter.add_pattern("*.CG")
    dialog.add_filter(filter)

    response = dialog.run()
    if response == gtk.RESPONSE_OK:
        try:
          if page != 0 or textbuffer[0].get_modified() == True:
            openfiles(self, sw[n+1], textbuffer[n+1], vistas, dialog.get_filename())
            textbuffer[n+1].set_modified(False)
            nfiles(self, dialog.get_filename(), 1)
          else:
            infiles=open(dialog.get_filename(),'r')
            if infiles:
              string = infiles.read()
              infiles.close()
              textbuffer[0].set_text(string)
            textbuffer[0].set_modified(False)
            nfiles(self, dialog.get_filename(), 3)
        except IOError :
            print "El fichero no existe."

    elif response == gtk.RESPONSE_CANCEL:
        print "No hay elementos seleccionados"
    dialog.destroy()

#guardar archivos
def savefile(self, sw, textbuffer, vistas):
        sw = sw
        textbuffer = textbuffer
        vistas = vistas

        page = vistas.get_current_page()
        filename = namefiles(self, page)

        if filename != "nuevo":
            try:
                texto=open(filename, 'w')
                texto.write(textbuffer[page].get_text(textbuffer[page].get_start_iter(), textbuffer[page].get_end_iter(), True)+"\n")
            except IOError :
                print "El fichero no existe."
            textbuffer[page].set_modified(False)
            texto.close()
        else:
            saveasfile(self, sw, textbuffer, vistas)

def saveasfile(self, sw, textbuffer, vistas):
        sw = sw
        textbuffer = textbuffer
        vistas = vistas
        page = vistas.get_current_page()
        filename = namefiles(self, page)
        print 'filename ', filename
        dialog = gtk.FileChooserDialog("Guardar archivo",None,
gtk.FILE_CHOOSER_ACTION_SAVE,(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
gtk.STOCK_SAVE, gtk.RESPONSE_OK))
        dialog.set_default_response(gtk.RESPONSE_OK)
        response = dialog.run()
        if response == gtk.RESPONSE_OK:
            try:
                texto = open(dialog.get_filename(), 'w')
                texto.write(textbuffer[page].get_text(textbuffer[page].get_start_iter(), textbuffer[page].get_end_iter(), True)+"\n")
                file = open('.archivo'+str(page)+'.dat', 'w')
                file.write(dialog.get_filename())
                file.close()
            except IOError :
                print "El fichero no existe."
            textbuffer[page].set_modified(False)
            texto.close()
        elif response == gtk.RESPONSE_CANCEL:
            print "No hay elementos seleccionados"

        label = gtk.Label(filename)
        label.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse('blue'))
        vistas.remove_page(page)
        vistas.insert_page(sw[page], label, page)
        #vistas.next_page()
        dialog.destroy()

def close(self, textbuffer, vistas):
    textbuffer = textbuffer
    vistas = vistas

    page = vistas.get_current_page()

    if textbuffer[page].get_modified() == True:
        changeverify(self, textbuffer[page], vistas, page)

    removefile(self, page)
    vistas.remove_page(page)

def removefile(self, page):
    page = page
    nfiles(self, 'None', 2)

    if page!= 0:
      os.system('rm .archivo'+str(page)+'.dat')

#cerrar la aplicación
def quit(self, textbuffer, vistas, window):
        textbuffer = textbuffer
        vistas = vistas
        window = window
        i=int(0)
        k=int(0)
        j=int(0)

        n = nfiles(self, 'None', 0)

        while i!=-1:
          file = os.system('ls .archivo'+str(k)+'.dat')
          print 'file: ', file
          if file != 512:
            print 'k = ', k
            if textbuffer[k].get_modified() == True:
              changeverify(self, textbuffer[k], vistas, k)
            j=j+1
          if k != 0:
              os.system('rm .archivo'+str(k)+'.dat')
          if j==n+1:
              i=-1
          k=k+1

        f = open('.n.dat', 'w')
        f1 = open('.archivo0.dat', 'w')
        f.write('0')
        f1.write('nuevo')
        f.close()
        f1.close()
        
        gtk.main_quit()

#Verificar modificaciones
def changeverify(self, textbuffer, vistas, page):
        textbuffer = textbuffer
        vistas = vistas
        page=page

        try:
          file = ['.archivo'+str(page)+'.dat']
          for line in file:
              f = open(line, 'r')
              filename = str(f.read())
          f.close()
        except IOError :
          print 'no existe el archivo'

        dialog = gtk.Dialog("Aviso", None, 0, (gtk.STOCK_NO, gtk.RESPONSE_CANCEL, gtk.STOCK_YES, gtk.RESPONSE_OK))
        dialog.set_default_response(gtk.RESPONSE_OK)
        label = gtk.Label('Tiene cambios sin guardar en el archivo'+filename+' '+str(page)+', desea guardar los cambios?')
        dialog.vbox.pack_start(label, True, True, 0)
        label.show()
        response = dialog.run()
        if response == gtk.RESPONSE_OK:
                return savefile(self, textbuffer, filename)
        elif response == gtk.RESPONSE_CANCEL:
                return False
        dialog.destroy()

#Buscar linea
def findline(self, textbuffer, vistas):
        textbuffer = textbuffer
        vistas = vistas
        
        page = vistas.get_current_page()
        textbuffer = textbuffer[page]
        
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
def result(self, textbuffer, sw1, statusbar, context_id):
        textbuffer = textbuffer
        sw1 = sw1
        statusbar = statusbar
        context_id = context_id

        completo = ""
        posicion = -1
        nolinea = -1
        
        textbuffer.delete(textbuffer.get_start_iter(), textbuffer.get_end_iter())

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

            os.system('rm lexico.cg')
        except IOError :
            for codigo in resultado2:
              f = open(codigo, 'r')
              if f:
                string = f.read()
                f.close()
                textbuffer.set_text(string)
            label.set_text("Sin errores léxicos")

        statusbar.push(context_id, label.get_text())
        
def Text(self, textbuffer):
        textbuffer = textbuffer

        self.inicio = textbuffer.get_start_iter()
        self.fin = textbuffer.get_end_iter()
        texto = textbuffer.get_text(self.inicio, self.fin, True)

        return texto

def ejecute(self, textbuffer, textbuffer1, sw1, statusbar, context_id, vistas):
        textbuffer = textbuffer
        textbuffer1 = textbuffer1
        sw1 = sw1
        statusbar = statusbar
        context_id = context_id
        vistas = vistas

        os.system('rm .*.cg')
        os.system('clear')
        page = vistas.get_current_page()
        texto = Text(self, textbuffer[page])
        if texto:
            lexico.lexico(texto)
        result(self, textbuffer1, sw1, statusbar, context_id)

#acerca de
def about(self):
        aboutdialog = gtk.AboutDialog()
        authors = ["Jorge Ortega", "Jesús Pérez"]
        logo = gtk.gdk.pixbuf_new_from_file_at_size('logoCG.png', 100, 100)
        comments = "Programa que permite dibujar figuras geométricas.\nMediante sentencias de programación.\nEs un proyecto de Compiladores."
        aboutdialog.set_program_name("CG: Compilador Geométrico")
        aboutdialog.set_logo(logo)
        aboutdialog.set_comments(comments)
        aboutdialog.set_copyright("GPL 3.0")
        aboutdialog.set_authors(authors)
        aboutdialog.set_website("http://code.google.com/p/compiladorg/")
        aboutdialog.set_website_label("CG - Compilador Geométrico Website")
        aboutdialog.set_title("Acerca de..")
        aboutdialog.connect("response", on_close)
        aboutdialog.show()

# cerrar la ventana de acerca
def on_close(self, parameter):
        self.destroy()
