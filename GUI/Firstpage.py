#! /usr/bin/env python
#  -*- coding: utf-8 -*-

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import Firstpage_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = firstPage (root)
    Firstpage_support.init(root, top)
    root.mainloop() 

w = None
def create_firstPage(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_firstPage(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = firstPage (w)
    Firstpage_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_firstPage():
    global w
    w.destroy()
    w = None

class firstPage:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x450+808+204")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1,  1)
        top.title("Signal Detecting Software")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        
        root.state('zoomed')
        
        self.txtWidthLength = tk.Label(top)
        self.txtWidthLength.place(relx=0.35, rely=0.222, height=84, width=449)
        self.txtWidthLength.configure(activebackground="#f9f9f9")
        self.txtWidthLength.configure(activeforeground="black")
        self.txtWidthLength.configure(background="#d9d9d9")
        self.txtWidthLength.configure(disabledforeground="#a3a3a3")
        self.txtWidthLength.configure(font="-family {Segoe UI} -size 20")
        self.txtWidthLength.configure(foreground="#000000")
        self.txtWidthLength.configure(highlightbackground="#d9d9d9")
        self.txtWidthLength.configure(highlightcolor="black")
        self.txtWidthLength.configure(text='''Type in width and length of room''')

        self.nextpagebutton1 = tk.Button(top)
        self.nextpagebutton1.place(relx=0.56, rely=0.578, height=34, width=117)
        self.nextpagebutton1.configure(activebackground="#ececec")
        self.nextpagebutton1.configure(activeforeground="#000000")
        self.nextpagebutton1.configure(background="#d9d9d9")
        self.nextpagebutton1.configure(disabledforeground="#a3a3a3")
        self.nextpagebutton1.configure(font="-family {Segoe UI} -size 15")
        self.nextpagebutton1.configure(foreground="#000000")
        self.nextpagebutton1.configure(highlightbackground="#d9d9d9")
        self.nextpagebutton1.configure(highlightcolor="black")
        self.nextpagebutton1.configure(pady="0")
        self.nextpagebutton1.configure(text='''Next''')

        self.givenWidth = tk.Entry(top)
        self.givenWidth.place(relx=0.417, rely=0.4, height=24, relwidth=0.2)
        self.givenWidth.configure(background="white")
        self.givenWidth.configure(disabledforeground="#a3a3a3")
        self.givenWidth.configure(font="TkFixedFont")
        self.givenWidth.configure(foreground="#000000")
        self.givenWidth.configure(highlightbackground="#d9d9d9")
        self.givenWidth.configure(highlightcolor="black")
        self.givenWidth.configure(insertbackground="black")
        self.givenWidth.configure(selectbackground="blue")
        self.givenWidth.configure(selectforeground="white")

        self.givenLength = tk.Entry(top)
        self.givenLength.place(relx=0.417, rely=0.489, height=24, relwidth=0.2)
        self.givenLength.configure(background="white")
        self.givenLength.configure(disabledforeground="#a3a3a3")
        self.givenLength.configure(font="TkFixedFont")
        self.givenLength.configure(foreground="#000000")
        self.givenLength.configure(highlightbackground="#d9d9d9")
        self.givenLength.configure(highlightcolor="black")
        self.givenLength.configure(insertbackground="black")
        self.givenLength.configure(selectbackground="blue")
        self.givenLength.configure(selectforeground="white")

        self.txtWidth = tk.Label(top)
        self.txtWidth.place(relx=0.36, rely=0.4, height=21, width=64)
        self.txtWidth.configure(activebackground="#f9f9f9")
        self.txtWidth.configure(activeforeground="black")
        self.txtWidth.configure(background="#d9d9d9")
        self.txtWidth.configure(disabledforeground="#a3a3a3")
        self.txtWidth.configure(font="-family {Segoe UI} -size 11")
        self.txtWidth.configure(foreground="#000000")
        self.txtWidth.configure(highlightbackground="#d9d9d9")
        self.txtWidth.configure(highlightcolor="black")
        self.txtWidth.configure(text='''Width:''')

        self.txtLength = tk.Label(top)
        self.txtLength.place(relx=0.35, rely=0.489, height=21, width=104)
        self.txtLength.configure(activebackground="#f9f9f9")
        self.txtLength.configure(activeforeground="black")
        self.txtLength.configure(background="#d9d9d9")
        self.txtLength.configure(disabledforeground="#a3a3a3")
        self.txtLength.configure(font="-family {Segoe UI} -size 11")
        self.txtLength.configure(foreground="#000000")
        self.txtLength.configure(highlightbackground="#d9d9d9")
        self.txtLength.configure(highlightcolor="black")
        self.txtLength.configure(text='''Length:''')



if __name__ == '__main__':
    vp_start_gui()





