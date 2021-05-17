#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
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

import Thirdpage_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    Thirdpage_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    Thirdpage_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x450+660+210")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1,  1)
        top.title("Details")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        root.state('zoomed')
        
        self.givenSSID = tk.Entry(top)
        self.givenSSID.place(relx=0.35, rely=0.222, height=30, relwidth=0.333)
        self.givenSSID.configure(background="white")
        self.givenSSID.configure(disabledforeground="#a3a3a3")
        self.givenSSID.configure(font="TkFixedFont")
        self.givenSSID.configure(foreground="#000000")
        self.givenSSID.configure(highlightbackground="#d9d9d9")
        self.givenSSID.configure(highlightcolor="black")
        self.givenSSID.configure(insertbackground="black")
        self.givenSSID.configure(selectbackground="blue")
        self.givenSSID.configure(selectforeground="white")

        self.givenMac1 = tk.Entry(top)
        self.givenMac1.place(relx=0.35, rely=0.333, height=30, relwidth=0.333)
        self.givenMac1.configure(background="white")
        self.givenMac1.configure(disabledforeground="#a3a3a3")
        self.givenMac1.configure(font="TkFixedFont")
        self.givenMac1.configure(foreground="#000000")
        self.givenMac1.configure(highlightbackground="#d9d9d9")
        self.givenMac1.configure(highlightcolor="black")
        self.givenMac1.configure(insertbackground="black")
        self.givenMac1.configure(selectbackground="blue")
        self.givenMac1.configure(selectforeground="white")

        self.givenMac2 = tk.Entry(top)
        self.givenMac2.place(relx=0.35, rely=0.444, height=30, relwidth=0.333)
        self.givenMac2.configure(background="white")
        self.givenMac2.configure(disabledforeground="#a3a3a3")
        self.givenMac2.configure(font="TkFixedFont")
        self.givenMac2.configure(foreground="#000000")
        self.givenMac2.configure(highlightbackground="#d9d9d9")
        self.givenMac2.configure(highlightcolor="black")
        self.givenMac2.configure(insertbackground="black")
        self.givenMac2.configure(selectbackground="blue")
        self.givenMac2.configure(selectforeground="white")

        self.givenMac3 = tk.Entry(top)
        self.givenMac3.place(relx=0.35, rely=0.556, height=30, relwidth=0.333)
        self.givenMac3.configure(background="white")
        self.givenMac3.configure(disabledforeground="#a3a3a3")
        self.givenMac3.configure(font="TkFixedFont")
        self.givenMac3.configure(foreground="#000000")
        self.givenMac3.configure(highlightbackground="#d9d9d9")
        self.givenMac3.configure(highlightcolor="black")
        self.givenMac3.configure(insertbackground="black")
        self.givenMac3.configure(selectbackground="blue")
        self.givenMac3.configure(selectforeground="white")

        self.SSIDtxt = tk.Label(top)
        self.SSIDtxt.place(relx=0.3, rely=0.222, height=30, width=85)
        self.SSIDtxt.configure(activebackground="#f9f9f9")
        self.SSIDtxt.configure(activeforeground="black")
        self.SSIDtxt.configure(background="#d9d9d9")
        self.SSIDtxt.configure(disabledforeground="#a3a3a3")
        self.SSIDtxt.configure(font="-family {Segoe UI} -size 11")
        self.SSIDtxt.configure(foreground="#000000")
        self.SSIDtxt.configure(highlightbackground="#d9d9d9")
        self.SSIDtxt.configure(highlightcolor="black")
        self.SSIDtxt.configure(text='''SSID''')

        self.mac1txt = tk.Label(top)
        self.mac1txt.place(relx=0.3, rely=0.333, height=30, width=85)
        self.mac1txt.configure(activebackground="#f9f9f9")
        self.mac1txt.configure(activeforeground="black")
        self.mac1txt.configure(background="#d9d9d9")
        self.mac1txt.configure(disabledforeground="#a3a3a3")
        self.mac1txt.configure(font="-family {Segoe UI} -size 11")
        self.mac1txt.configure(foreground="#000000")
        self.mac1txt.configure(highlightbackground="#d9d9d9")
        self.mac1txt.configure(highlightcolor="black")
        self.mac1txt.configure(text='''Mac 1''')

        self.mac2txt = tk.Label(top)
        self.mac2txt.place(relx=0.3, rely=0.444, height=30, width=85)
        self.mac2txt.configure(activebackground="#f9f9f9")
        self.mac2txt.configure(activeforeground="black")
        self.mac2txt.configure(background="#d9d9d9")
        self.mac2txt.configure(disabledforeground="#a3a3a3")
        self.mac2txt.configure(font="-family {Segoe UI} -size 11")
        self.mac2txt.configure(foreground="#000000")
        self.mac2txt.configure(highlightbackground="#d9d9d9")
        self.mac2txt.configure(highlightcolor="black")
        self.mac2txt.configure(text='''Mac 2''')

        self.mac3txt = tk.Label(top)
        self.mac3txt.place(relx=0.3, rely=0.556, height=30, width=85)
        self.mac3txt.configure(activebackground="#f9f9f9")
        self.mac3txt.configure(activeforeground="black")
        self.mac3txt.configure(background="#d9d9d9")
        self.mac3txt.configure(disabledforeground="#a3a3a3")
        self.mac3txt.configure(font="-family {Segoe UI} -size 11")
        self.mac3txt.configure(foreground="#000000")
        self.mac3txt.configure(highlightbackground="#d9d9d9")
        self.mac3txt.configure(highlightcolor="black")
        self.mac3txt.configure(text='''Mac 3''')

        self.calculateButton = tk.Button(top)
        self.calculateButton.place(relx=0.3, rely=0.711, height=34, width=187)
        self.calculateButton.configure(activebackground="#ececec")
        self.calculateButton.configure(activeforeground="#000000")
        self.calculateButton.configure(background="#d9d9d9")
        self.calculateButton.configure(disabledforeground="#a3a3a3")
        self.calculateButton.configure(font="-family {Segoe UI} -size 15")
        self.calculateButton.configure(foreground="#000000")
        self.calculateButton.configure(highlightbackground="#d9d9d9")
        self.calculateButton.configure(highlightcolor="black")
        self.calculateButton.configure(pady="0")
        self.calculateButton.configure(text='''Calculate''')

if __name__ == '__main__':
    vp_start_gui()





