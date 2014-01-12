#! /usr/bin/python
# -*- coding: utf-8 -*-

import ply.lex as lex
import pygtk
import gtk
import os
import tokens
import funtions as funtion

class Interfaz:
    ui = '''<ui>
    <menubar name="MenuBar">
      <menu action="File">
        <menuitem action="New"/>
        <menuitem action="Open"/>
        <menuitem action="Save"/>
        <menuitem action="Save_As"/>
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
      </menu>
    </menubar>
    <toolbar name="Toolbar">
      <toolitem action="New"/>
      <separator/>
      <toolitem action="Save"/>
      <separator/>
      <toolitem action="Quit"/>
      <separator/>
      <toolitem action="Convert"/>
      <separator/>
    </toolbar>
    </ui>'''

    def __init__(self): 
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_resizable(True)  
        window.connect('destroy', lambda w: gtk.main_quit())
        window.set_title("Archivo nuevo sin guardar")
        window.set_size_request(800, 700)
        window.set_border_width(5)

        vistas = gtk.Notebook()
        vistas.set_tab_pos(gtk.POS_RIGHT)

        box1 = gtk.VBox(False, 0)
        window.add(box1)
        filename = 'None'
        box1.show()

        box2 = gtk.VBox(False, 10)
        box2.set_border_width(10)
        box1.pack_start(box2, True, True, 0)
        box2.show()

        sw = gtk.ScrolledWindow()
        sw.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        textview = gtk.TextView()
        textbuffer = textview.get_buffer()
        sw.add(textview)
        sw.show()
        textview.show()

        label = gtk.Label("Fuente")
        label.show()
        vistas.append_page(sw, label)

        sw1 = gtk.ScrolledWindow()
        sw1.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        textview1 = gtk.TextView()
        textview1.set_editable(False)
        textbuffer1 = textview1.get_buffer()
        sw1.add(textview1)
        sw1.show()
        textview1.show()

        # creamos una barra de estado
        statusbar = gtk.Statusbar()
        context_id = statusbar.get_context_id("")
        statusbar.push(context_id, " ")
        tag = textbuffer.create_tag(None, foreground="red")

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
            ('Quit', gtk.STOCK_QUIT, None, '<Control>q', 'Quit programa'),
            ('File', None, '_Archivo'),
            ('Find_line', gtk.STOCK_FIND, None, '<Control>i', 'Buscar linea'),
            ('Go', None, '_Ir'),
            ('Lexico', None, 'Léxico', '<Control>l', 'Léxico'),
            ('Syntactic', None, 'Sintáctico', '<Control>y', 'Sintáctico'),
            ('Semantic', None, 'Semántico', '<Control>z', 'Semántico'),
            ('Analyc', None, 'Analizar'),
            ('Convert', None, 'Dibujar', '<Control>d', 'Semántico'),
            ('Tools', None, '_Herramientas'),
            ('About', gtk.STOCK_ABOUT, None, '<Control>u', 'Acerca de'),
            ('Help', None, 'Ay_uda')
        ])

        #conectamos los eventos
        actiongroup.get_action('New').connect('activate', funtion.new, textbuffer, window, vistas)
        actiongroup.get_action('Open').connect('activate', funtion.openfile, textbuffer, window)
        actiongroup.get_action('Save').connect('activate', funtion.savefile, textbuffer, window)
        actiongroup.get_action('Save_As').connect('activate', funtion.saveasfile, textbuffer, window)
        actiongroup.get_action('Quit').connect('activate', funtion.close, textbuffer, window)
        actiongroup.get_action('Find_line').connect('activate', funtion.findline, textbuffer)
        actiongroup.get_action('Lexico').connect('activate', funtion.ejecute, textbuffer, textbuffer1, vistas, sw1, statusbar, context_id)
        actiongroup.get_action('About').connect('activate', funtion.about)

        uimanager.insert_action_group(actiongroup, 0)
        uimanager.add_ui_from_string(self.ui)
        menubar = uimanager.get_widget('/MenuBar')
        box2.pack_start(menubar, False, True, 0)
        #menubar.show()

        separator = gtk.HSeparator()
        box2.pack_start(separator, False, True, 0)
        separator.show()

        box2.pack_start(vistas)
        box2.pack_start(statusbar, False, False, 0)
        vistas.show()
        statusbar.show()
        show_tabs = True
        show_border = True

        window.show()

def main():
    gtk.main()
    return 0       

if __name__ == "__main__":
    Interfaz()
    main()
