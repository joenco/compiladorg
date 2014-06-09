#! /usr/bin/python
# -*- coding: utf-8 -*-

import ply.lex as lex
import pygtk
import gtk
import os
import lexico
import parserCG
import funtions as funtion
import  tabladesimbolos as funtion1

class Interfaz:
    ui = '''<ui>
    <menubar name="MenuBar">
      <menu action="File">
        <menuitem action="New"/>
        <menuitem action="Open"/>
        <menuitem action="Save"/>
        <menuitem action="Save_As"/>
        <menuitem action="Close"/>
        <menuitem action="Quit"/>
      </menu>
      <menu action="Go">
        <menuitem action="Find_line"/>
      </menu>
      <menu action="Tools">
        <menu action="Analyc">
          <menuitem action="Lexico"/>
          <menuitem action="Syntactic"/>
          <menuitem action="Semantic"/>
        </menu>
        <menuitem action="Convert"/>
      </menu>
      <menu action="Help">
        <menuitem action="About"/>
        <menuitem action="Tutor"/>
      </menu>
    </menubar>
    </ui>'''

    def __init__(self): 
    
        atributos = funtion1.preferencias(self)
        if atributos[0] == str(0):
          funtion.bienvenida(self)
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_resizable(True)  
        window.connect('destroy', lambda w: gtk.main_quit())
        window.set_title("Compilador Geometrico")
        window.set_size_request(800, 700)
        window.set_border_width(5)

        tabla = gtk.Table(800, 700, False)
        vistas = gtk.Notebook()
        vistas.set_tab_pos(gtk.POS_RIGHT)

        box1 = gtk.HBox(False, 0)
        window.add(tabla)
        box1.show()
        #box1.pack_start(tabla, True, True, 0)
        sw= []
        textview = []
        textbuffer = []

        for i in range(10):
            sw.append(i)
            textview.append(i)
            textbuffer.append(i)
            sw[i] = gtk.ScrolledWindow()
            sw[i].set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
            textview[i] = gtk.TextView()
            textbuffer[i] = textview[i].get_buffer()
            sw[i].add(textview[i])
            sw[i].show()
            textview[i].show()

        label = gtk.Label("Codigo Fuente")
        label.modify_fg(gtk.STATE_NORMAL,gtk.gdk.color_parse('blue'))
        label.show()
        vistas.append_page(sw[0], label)

        swl = gtk.ScrolledWindow()
        swl.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        textviewl = gtk.TextView()
        textviewl.set_editable(False)
        textbufferl = textviewl.get_buffer()
        swl.add(textviewl)
        swl.show()
        textviewl.show()

        # creamos una barra de estado
        statusbar = gtk.Statusbar()
        context_id = statusbar.get_context_id("")
        statusbar.push(context_id, " ")

        uimanager = gtk.UIManager()
        accelgroup = uimanager.get_accel_group()
        window.add_accel_group(accelgroup)

        actiongroup = gtk.ActionGroup('Interfaz')
        self.actiongroup = actiongroup

        actiongroup.add_actions([
            ('New', gtk.STOCK_NEW, None, '<Control>n', 'Nuevo archivo'),
            ('Open', gtk.STOCK_OPEN, None, '<Control>o', 'Abrir archivo'),
            ('Save', gtk.STOCK_SAVE, None, '<Control>g', 'Guardar archivo'),
            ('Save_As', gtk.STOCK_SAVE_AS, None, '<Control>s', 'Guardar archivo'),
            ('Close', gtk.STOCK_CLOSE, None, '<Control>w', 'Cierra la ventana'),
            ('Quit', gtk.STOCK_QUIT, None, '<Control>q', 'Cierra el programa'),
            ('File', None, '_Archivo'),
            ('Find_line', gtk.STOCK_FIND, None, '<Control>i', 'Buscar linea'),
            ('Go', None, '_Ir'),
            ('Lexico', None, 'Léxico', '<Control>l', 'Léxico'),
            ('Syntactic', None, 'Sintáctico', '<Control>y', 'Sintáctico'),
            ('Semantic', None, 'Semántico', '<Control>z', 'Semántico'),
            ('Analyc', None, 'Analizar'),
            ('Convert', None, 'Dibujar', '<Control>d', 'Dibujar'),
            ('Tools', None, '_Herramientas'),
            ('Tutor', gtk.STOCK_HELP, None, '<Control>h', 'La ayuda del programa'),
            ('About', gtk.STOCK_ABOUT, None, '<Control>u', 'Acerca de'),
            ('Help', None, 'Ay_uda')
        ])

        #conectamos los eventos
        actiongroup.get_action('New').connect('activate', funtion.new, sw, textbuffer, vistas)
        actiongroup.get_action('Open').connect('activate', funtion.openfile, sw, textbuffer, vistas)
        actiongroup.get_action('Save').connect('activate', funtion.savefile, sw, textbuffer, vistas, 1)
        actiongroup.get_action('Save_As').connect('activate', funtion.saveasfile, sw, textbuffer, vistas, 1)
        actiongroup.get_action('Close').connect('activate', funtion.close, sw, textbuffer, vistas)
        actiongroup.get_action('Quit').connect('activate', funtion.quit, sw, textbuffer, vistas, window)
        actiongroup.get_action('Find_line').connect('activate', funtion.findline, textbuffer, vistas)
        actiongroup.get_action('Lexico').connect('activate', funtion.ejecute, textbuffer, textbufferl, swl, statusbar, context_id, vistas, 1)
        actiongroup.get_action('Syntactic').connect('activate', funtion.ejecute, textbuffer, textbufferl, swl, statusbar, context_id, vistas, 2)
        actiongroup.get_action('Convert').connect('activate', funtion.ejecute, textbuffer, textbufferl, swl, statusbar, context_id, vistas, 3)
        actiongroup.get_action('About').connect('activate', funtion.about)

        uimanager.insert_action_group(actiongroup, 0)
        uimanager.add_ui_from_string(self.ui)
        menubar = uimanager.get_widget('/MenuBar')
        handlebox = gtk.HandleBox()
        toolbar = funtion.toolbar(self, sw, swl, vistas, textbuffer, textbufferl, statusbar, context_id)
        handlebox.add(toolbar)
        handlebox.show()

        #imageanime = gtk.gdk.PixbufAnimation("imagenes/banerCG.gif")
        #image = gtk.Image()
        #self.image.set_from_animation(imageanime)
        image = gtk.Image()
        image.set_from_file('imagenes/banerCG.png')
        image.show()
        tabla.attach(image, 0, 700, 0, 3)
        tabla.attach(menubar, 0, 700, 4, 6)

        separator = gtk.HSeparator()
        #toolbar = uimanager.get_widget('/Toolbar')
        toolbar.show()
        tabla.attach(handlebox, 0, 700, 7, 9)
        separator.show()

        tabla.attach(vistas, 0, 700, 10, 200)
        tabla.attach(statusbar, 0, 650, 760, 761)
        tabla.attach(swl, 0, 650, 762, 800)
        vistas.show()

        statusbar.show()
        show_tabs = True
        show_border = True

        tabla.show()

        window.show()

def main():
    gtk.main()
    return 0       

if __name__ == "__main__":
    Interfaz()
    main()
