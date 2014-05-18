#! /usr/bin/python
# -*- coding: utf-8 -*-

import ply.lex as lex
import pygtk
import gtk
import os
import lexico
import parserCG
import funtiontable as funtion
import figuras
import tabladesimbolos as funtion1

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
    filename = namefiles(self, 0)

    if n>0 or textbuffer[0].get_modified() == True or filename!='nuevo':
        openfiles(self, sw[n+1], textbuffer[n+1], vistas, 'Nuevo')
        nfiles(self, 'nuevo', 1)

#Abrir archivo
def openfile(self, sw, textbuffer, vistas):
    sw = sw
    textbuffer = textbuffer
    vistas=vistas
    
    page = vistas.get_current_page()
    n = nfiles(self, 'None', 0)
    filename = namefiles(self, 0)

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
          if page != 0 or textbuffer[0].get_modified() == True or filename != 'nuevo':
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
            narchivo = funtion1.nombre(self, dialog.get_filename())
            label = gtk.Label(narchivo)
            label.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse('blue'))
            vistas.remove_page(page)
            vistas.insert_page(sw[page], label, page)
        except IOError :
            print "El fichero no existe."

    elif response == gtk.RESPONSE_CANCEL:
        print "No hay elementos seleccionados"
    dialog.destroy()

#guardar archivos
def savefile(self, sw, textbuffer, vistas, remove):
        sw = sw
        textbuffer = textbuffer
        vistas = vistas
        remove = remove

        page = vistas.get_current_page()
        filename = namefiles(self, page)

        if filename != "nuevo":
            texto=open(filename, 'w')
            texto.write(textbuffer[page].get_text(textbuffer[page].get_start_iter(), textbuffer[page].get_end_iter(), True)+"\n")
            textbuffer[page].set_modified(False)
            texto.close()
        else:
            saveasfile(self, sw, textbuffer, vistas, remove)

#guardar como
def saveasfile(self, sw, textbuffer, vistas, remove):
        sw = sw
        textbuffer = textbuffer
        vistas = vistas
        remove = remove
        page = vistas.get_current_page()
        filename = namefiles(self, page)
        print 'filename ', filename
        dialog = gtk.FileChooserDialog("Guardar archivo",None,
gtk.FILE_CHOOSER_ACTION_SAVE,(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
gtk.STOCK_SAVE, gtk.RESPONSE_OK))
        dialog.set_default_response(gtk.RESPONSE_OK)
        response = dialog.run()
        if response == gtk.RESPONSE_OK:
            texto = open(dialog.get_filename(), 'w')
            texto.write(textbuffer[page].get_text(textbuffer[page].get_start_iter(), textbuffer[page].get_end_iter(), True)+"\n")
            file = open('.archivo'+str(page)+'.dat', 'w')
            file.write(dialog.get_filename())
            file.close()
            textbuffer[page].set_modified(False)
            texto.close()
            narchivo = funtion1.nombre(self, dialog.get_filename())
            label = gtk.Label(narchivo)
            label.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse('blue'))
            if remove==1:
              vistas.remove_page(page)
              vistas.insert_page(sw[page], label, page)
        elif response == gtk.RESPONSE_CANCEL:
            print "No hay elementos seleccionados"

        dialog.destroy()

def close(self, sw, textbuffer, vistas):
    sw = sw
    textbuffer = textbuffer
    vistas = vistas

    page = vistas.get_current_page()

    if textbuffer[page].get_modified() == True:
        changeverify(self, sw, textbuffer, vistas, page, 0)

    removefile(self, vistas, page)

def removefile(self, vistas, page):
    vistas = vistas
    page = page
    nfiles(self, 'None', 2)

    if page!= 0:
      os.system('rm .archivo'+str(page)+'.dat')
    vistas.remove_page(page)

#cerrar la aplicación
def quit(self, sw, textbuffer, vistas, window):
        sw = sw
        textbuffer = textbuffer
        vistas = vistas
        window = window
        i=int(0)
        k=int(0)
        j=int(0)

        n = nfiles(self, 'None', 0)

        while i!=-1:
          file = os.system('ls .archivo'+str(k)+'.dat')
          if file != 512:
            if textbuffer[k].get_modified() == True:
              changeverify(self, sw, textbuffer, vistas, k, 1)
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
        os.system('rm .*cg')
        gtk.main_quit()

# guarda o no las modificaciones
def changeverify(self, sw, textbuffer, vistas, page, remove):
        sw = sw
        textbuffer = textbuffer
        vistas = vistas
        page=page
        remove = remove

        filename = namefiles(self, page)

        dialog = gtk.Dialog("Aviso", None, 0, (gtk.STOCK_NO, gtk.RESPONSE_CANCEL, gtk.STOCK_YES, gtk.RESPONSE_OK))
        dialog.set_default_response(gtk.RESPONSE_OK)
        if filename != 'nuevo':
            label = gtk.Label('Tiene cambios sin guardar en el archivo'+filename+', desea guardar los cambios?')
        else:
            label = gtk.Label('Tiene cambios sin guardar en el archivo'+filename+' '+str(page)+', desea guardar los cambios?')
        dialog.vbox.pack_start(label, True, True, 0)
        label.show()
        response = dialog.run()
        if response == gtk.RESPONSE_OK:
            print "se ha presionado Si"
            return savefile(self, sw, textbuffer, vistas, remove)
            #dialog.destroy()
        elif response == gtk.RESPONSE_CANCEL:
            print "se ha presionado No"
            #dialog.destroy()
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
            try:
                for codigo in resultado2:
                  f = open(codigo, 'r')
                  if f:
                    string = f.read()
                    f.close()
                    textbuffer.set_text(string)
                label.set_text("Sin errores léxicos")
            except IOError :
                print "Error al leer .tokens.cg"
        statusbar.push(context_id, label.get_text())

#Analisis sintactico
def result2(self, textbuffer, sw1, statusbar, context_id):
        textbuffer = textbuffer
        sw1 = sw1
        statusbar = statusbar
        context_id = context_id

        textbuffer.delete(textbuffer.get_start_iter(), textbuffer.get_end_iter())

        resultado2 = ['.erroresSintaxis.cg']
        label = gtk.Label()
        
        primero = True

        try:
            f = open (".errorSintaxis.cg",'r')
            errores=open('.erroresSintaxis.cg', 'a')
            for line in f.readlines():
                separados = line.split(':',2)
                actual = str(separados[0])
                lexema = str(separados[1])
                
                if primero == True:
                    primero = False
                    anterior = actual
                    if lexema != "fin":
                        errores.write("Error sintactico en la linea "+actual+" en el lexema " + lexema+"\n")
                    else:
                        errores.write("Error sintactico en la linea "+actual+"\n")
                if actual != anterior:
                    if lexema != "fin":
                        errores.write("Error sintactico en la linea "+actual+" en el lexema " + lexema+"\n")
                    else:
                        errores.write("Error sintactico en la linea "+actual+"\n")
                    anterior = actual
            errores.close()
            f.close()
        except IOError :
            print "El Analizador Sintactico no encontro errores"
                
        for codigo in resultado2:
            try:
            	f = open(codigo, 'r')
            	if f:
                	string = f.read()
               		f.close()
                	textbuffer.set_text(string)
            	label.set_text("Errores de sintaxis")
            except IOError :
                #print "Error al abrir .erroresSintaxis.cg"
		label.set_text("No hay errores de sintaxis")

        statusbar.push(context_id, label.get_text())

        
def Text(self, textbuffer):
        textbuffer = textbuffer
        nline = textbuffer.get_line_count()

        self.inicio = textbuffer.get_start_iter()
        self.fin = textbuffer.get_end_iter()
        texto = textbuffer.get_text(self.inicio, self.fin, True)
        for i in range(nline):
          lineas = texto.splitlines()
        #simbolos =funtion.simbolos(texto, lineas)
        #print simbolos

        return texto

def Draw(self, textbuffer):
        textbuffer = textbuffer
        nline = textbuffer.get_line_count()

        self.inicio = textbuffer.get_start_iter()
        self.fin = textbuffer.get_end_iter()
        texto = textbuffer.get_text(self.inicio, self.fin, True)
        for i in range(nline):
          lineas = texto.splitlines()
        simbolos = funtion.simbolos(texto, lineas)
        #print simbolos
	figuras.dibujar(simbolos)

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

def ejecute2(self, textbuffer, textbuffer1, sw1, statusbar, context_id, vistas):
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
            parserCG.parse(texto)
        result2(self, textbuffer1, sw1, statusbar, context_id)

def ejecute3(self, textbuffer, vistas):
        textbuffer = textbuffer
        vistas = vistas

        os.system('rm .*.cg')
        os.system('clear')

        page = vistas.get_current_page()
        texto = Draw(self, textbuffer[page])

#acerca de
def about(self):
        aboutdialog = gtk.AboutDialog()
        authors = ["Jorge Ortega", "Jesús Pérez"]
        logo = gtk.gdk.pixbuf_new_from_file_at_size('imagenes/logoCG.png', 100, 100)
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

def icon(self, icons):
    icons = icons
    icon = gtk.Image()
    icon.set_from_file(icons)

    return icon

def toolbar(self, sw, vistas, textbuffer):
        sw = sw
        vistas = vistas
        textbuffer = textbuffer
        toolbar = gtk.Toolbar()
        toolbar.set_orientation(gtk.ORIENTATION_HORIZONTAL)
        toolbar.set_style(gtk.TOOLBAR_ICONS)
        toolbar.set_border_width(5)


        iconnew = icon(self, 'imagenes/nuevo.xpm')
        bnew = toolbar.append_item("Nuevo", "Nuevo archivo","Private", iconnew, None)
        bnew.connect('activate', new, sw, textbuffer, vistas)
        toolbar.append_space()
        iconopen = icon(self, 'imagenes/abrir.xpm')
        bopen = toolbar.append_item("Abrir", "Abrir archivo", "Private", iconopen, None)
        bopen.connect('activate', openfile, sw, textbuffer, vistas)
        toolbar.append_space()
        iconsave = icon(self, 'imagenes/guardar.xpm')
        bsave = toolbar.append_item("Guardar", "Guardar el archivo", "Private", iconsave, None)
        bsave.connect('activate', savefile, sw, textbuffer, vistas, 1)
        toolbar.append_space()
        icondraw = icon(self, 'imagenes/dibujar.xpm')
        bdraw = toolbar.append_item("Dibujar", "Dibujar el archivo", "Private", icondraw, None)
        bdraw.connect('activate', ejecute3, textbuffer, vistas)
        toolbar.append_space()

        return toolbar
