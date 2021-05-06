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

import Secondpage_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel (root)
    Secondpage_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel (w)
    Secondpage_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel():
    global w
    w.destroy()
    w = None

class Toplevel:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x450+785+211")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1,  1)
        top.title("Placement of the anchors")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.txtTheRoom = tk.Label(top)
        self.txtTheRoom.place(relx=0.367, rely=0.178, height=31, width=124)
        self.txtTheRoom.configure(activebackground="#f9f9f9")
        self.txtTheRoom.configure(activeforeground="black")
        self.txtTheRoom.configure(background="#d9d9d9")
        self.txtTheRoom.configure(disabledforeground="#a3a3a3")
        self.txtTheRoom.configure(font="-family {Segoe UI} -size 15")
        self.txtTheRoom.configure(foreground="#000000")
        self.txtTheRoom.configure(highlightbackground="#d9d9d9")
        self.txtTheRoom.configure(highlightcolor="black")
        self.txtTheRoom.configure(text='''The Room''')

        self.CanvasRoom = tk.Canvas(top)
        self.CanvasRoom.place(relx=0.367, rely=0.267, relheight=0.384
                , relwidth=0.205)
        self.CanvasRoom.configure(background="#d9d9d9")
        self.CanvasRoom.configure(borderwidth="2")
        self.CanvasRoom.configure(highlightbackground="#d9d9d9")
        self.CanvasRoom.configure(highlightcolor="black")
        self.CanvasRoom.configure(insertbackground="black")
        self.CanvasRoom.configure(relief="ridge")
        self.CanvasRoom.configure(selectbackground="blue")
        self.CanvasRoom.configure(selectforeground="white")

        self.descriptiontxt = tk.Label(top)
        self.descriptiontxt.place(relx=0.25, rely=0.667, height=31, width=284)
        self.descriptiontxt.configure(activebackground="#f9f9f9")
        self.descriptiontxt.configure(activeforeground="black")
        self.descriptiontxt.configure(background="#d9d9d9")
        self.descriptiontxt.configure(disabledforeground="#a3a3a3")
        self.descriptiontxt.configure(font="-family {Segoe UI} -size 14")
        self.descriptiontxt.configure(foreground="#000000")
        self.descriptiontxt.configure(highlightbackground="#d9d9d9")
        self.descriptiontxt.configure(highlightcolor="black")
        self.descriptiontxt.configure(text='''Put the access points right here''')

        self.nextButton = tk.Button(top)
        self.nextButton.place(relx=0.367, rely=0.778, height=34, width=120)
        self.nextButton.configure(activebackground="#ececec")
        self.nextButton.configure(activeforeground="#000000")
        self.nextButton.configure(background="#d9d9d9")
        self.nextButton.configure(disabledforeground="#a3a3a3")
        self.nextButton.configure(font="-family {Segoe UI} -size 15")
        self.nextButton.configure(foreground="#000000")
        self.nextButton.configure(highlightbackground="#d9d9d9")
        self.nextButton.configure(highlightcolor="black")
        self.nextButton.configure(pady="0")
        self.nextButton.configure(text='''Next''')

if __name__ == '__main__':
    vp_start_gui()





