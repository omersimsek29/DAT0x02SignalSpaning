# -*- coding: utf-8 -*-
"""
Created on Tue May 18 23:11:12 2021

@author: simse
"""
import time
import tkinter as tk  
root = tk.Tk() 
result_output = [1,2]
index = 0
ssid = 0

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Page1(Page):
    def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)

       root.state('zoomed')
       
       txtWidthLength = tk.Label(self, text = "Type in width and length of Room")
       txtWidthLength.place(relx=0.35, rely=0.222, height=84, width=449)
       txtWidthLength.configure(disabledforeground="#a3a3a3")
       txtWidthLength.configure(font="-family {Segoe UI} -size 20")
       txtWidthLength.configure(foreground="#000000")
       txtWidthLength.configure(highlightbackground="#d9d9d9")
       txtWidthLength.configure(highlightcolor="black")
       txtWidthLength.configure(text='''Type in width and length of room''')


       self.givenWidth = tk.Entry(self)
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

       self.givenLength = tk.Entry(self)
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

       txtWidth = tk.Label(self, text = "Width:")
       txtWidth.place(relx=0.36, rely=0.4, height=21, width=64)
       txtWidth.configure(activebackground="#f9f9f9")
       txtWidth.configure(activeforeground="black")
       txtWidth.configure(disabledforeground="#a3a3a3")
       txtWidth.configure(font="-family {Segoe UI} -size 11")
       txtWidth.configure(foreground="#000000")
       txtWidth.configure(highlightbackground="#d9d9d9")
       txtWidth.configure(highlightcolor="black")
       txtWidth.configure(text='''Width:''')

       txtLength = tk.Label(self, text = "Length:")
       txtLength.place(relx=0.35, rely=0.489, height=21, width=104)
       txtLength.configure(activebackground="#f9f9f9")
       txtLength.configure(activeforeground="black")
       txtLength.configure(disabledforeground="#a3a3a3")
       txtLength.configure(font="-family {Segoe UI} -size 11")
       txtLength.configure(foreground="#000000")
       txtLength.configure(highlightbackground="#d9d9d9")
       txtLength.configure(highlightcolor="black")
       txtLength.configure(text='''Length:''')
    
class Page2(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       
       root.state('zoomed')
        
       txtTheRoom = tk.Label(self, text = "The Room")
       txtTheRoom.place(relx=0.367, rely=0.22, height=31, width=124)
       txtTheRoom.configure(activebackground="#f9f9f9")
       txtTheRoom.configure(activeforeground="black")
       txtTheRoom.configure(disabledforeground="#a3a3a3")
       txtTheRoom.configure(font="-family {Segoe UI} -size 15")
       txtTheRoom.configure(foreground="#000000")
       txtTheRoom.configure(highlightbackground="#d9d9d9")
       txtTheRoom.configure(highlightcolor="black")
       txtTheRoom.configure(text='''The Room''')

       CanvasRoom = tk.Canvas(self)
       CanvasRoom.place(relx=0.367, rely=0.267, relheight=0.384, relwidth=0.205)
       CanvasRoom.configure(borderwidth="2")
       CanvasRoom.configure(highlightbackground="#d9d9d9")
       CanvasRoom.configure(highlightcolor="black")
       CanvasRoom.configure(insertbackground="black")
       CanvasRoom.configure(relief="ridge")
       CanvasRoom.configure(selectbackground="blue")
       CanvasRoom.configure(selectforeground="white")
       CanvasRoom.create_rectangle(30, 10, 360, 360,
    outline="#000", fill="")
       CanvasRoom.create_oval(30, 10, 80, 80, outline="#f11",
    fill="", width=1)
     
    
       descriptiontxt = tk.Label(self, text ="Put the access points right here")
       descriptiontxt.place(relx=0.367, rely=0.667, height=31, width=284)
       descriptiontxt.configure(activebackground="#f9f9f9")
       descriptiontxt.configure(activeforeground="black")
       descriptiontxt.configure(disabledforeground="#a3a3a3")
       descriptiontxt.configure(font="-family {Segoe UI} -size 14")
       descriptiontxt.configure(foreground="#000000")
       descriptiontxt.configure(highlightbackground="#d9d9d9")
       descriptiontxt.configure(highlightcolor="black")
       descriptiontxt.configure(text='''Put the access points right here''')
         


class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       self.ssid="" 
       self.mac1=""
       self.mac2 =""
       self.mac3=""
       
       self.givenSSID = tk.Entry(self)
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

       self.givenMac1 = tk.Entry(self)
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

       self.givenMac2 = tk.Entry(self)
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

       self.givenMac3 = tk.Entry(self)
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

       SSIDtxt = tk.Label(self, text ="SSID")
       SSIDtxt.place(relx=0.3, rely=0.222, height=30, width=85)
       SSIDtxt.configure(activebackground="#f9f9f9")
       SSIDtxt.configure(activeforeground="black")
       SSIDtxt.configure(disabledforeground="#a3a3a3")
       SSIDtxt.configure(font="-family {Segoe UI} -size 11")
       SSIDtxt.configure(foreground="#000000")
       SSIDtxt.configure(highlightbackground="#d9d9d9")
       SSIDtxt.configure(highlightcolor="black")
       SSIDtxt.configure(text='''SSID''')

       mac1txt = tk.Label(self, text ="MAC 1")
       mac1txt.place(relx=0.3, rely=0.333, height=30, width=85)
       mac1txt.configure(activebackground="#f9f9f9")
       mac1txt.configure(activeforeground="black")
       mac1txt.configure(disabledforeground="#a3a3a3")
       mac1txt.configure(font="-family {Segoe UI} -size 11")
       mac1txt.configure(foreground="#000000")
       mac1txt.configure(highlightbackground="#d9d9d9")
       mac1txt.configure(highlightcolor="black")
       mac1txt.configure(text='''MAC 1''')

       mac2txt = tk.Label(self, text ="MAC 2")
       mac2txt.place(relx=0.3, rely=0.444, height=30, width=85)
       mac2txt.configure(activebackground="#f9f9f9")
       mac2txt.configure(activeforeground="black")
       mac2txt.configure(disabledforeground="#a3a3a3")
       mac2txt.configure(font="-family {Segoe UI} -size 11")
       mac2txt.configure(foreground="#000000")
       mac2txt.configure(highlightbackground="#d9d9d9")
       mac2txt.configure(highlightcolor="black")
       mac2txt.configure(text='''MAC 2''')

       mac3txt = tk.Label(self, text ="MAC 3")
       mac3txt.place(relx=0.3, rely=0.556, height=30, width=85)
       mac3txt.configure(activebackground="#f9f9f9")
       mac3txt.configure(activeforeground="black")
       mac3txt.configure(disabledforeground="#a3a3a3")
       mac3txt.configure(font="-family {Segoe UI} -size 11")
       mac3txt.configure(foreground="#000000")
       mac3txt.configure(highlightbackground="#d9d9d9")
       mac3txt.configure(highlightcolor="black")
       mac3txt.configure(text='''MAC 3''')
   
   def get_ssid(self):
       self.ssid = self.givenSSID.get()
       
       print(str(self.ssid))
   
   def get_mac1(self):
        self.mac1 = self.givenMac1.get()
        
        return self.mac1
    
   def get_mac2(self):
       self.mac2 = self.givenMac2.get()
       
       return self.mac2
   
   def get_mac3(self):
       self.mac3 = self.givenMac3.get()

       return self.mac3
    
class Page4(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
      
       self.Scrolledtext1 = tk.Text(self)
       self.vsb = tk.Scrollbar(self, orient="vertical", command=self.Scrolledtext1.yview)
       self.Scrolledtext1.configure(yscrollcommand=self.vsb.set)
       self.vsb.pack(side="right", fill="y")
       self.Scrolledtext1.place(relx=0.083, rely=0.133, relheight=0.744, relwidth=0.417)

       self.Canvas1 = tk.Canvas(self)
       self.Canvas1.place(relx=0.517, rely=0.133, relheight=0.744, relwidth=0.417)
       self.Canvas1.configure(background="#d9d9d9")
       self.Canvas1.configure(borderwidth="2")
       self.Canvas1.configure(insertbackground="black")
       self.Canvas1.configure(relief="ridge")
       self.Canvas1.configure(selectbackground="blue")
       self.Canvas1.configure(selectforeground="white")
       self.print_result()
   
   def print_result(self):
      global index
      
      if len(result_output) > index and len(result_output) != 0: 
          self.Scrolledtext1.insert("end", str(result_output[index]) + "\n")
          index+=1
          
   #   self.Scrolledtext1.insert("end", time.ctime() + "\n")
   #   self.Scrolledtext1.see("end")
   #  self.after(1000, self.print_result)  

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)
        p4 = Page4(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)
        
        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        
        b1 = tk.Button(buttonframe, text="Step 1",font="-family {Segoe UI} -size 13", height=1, width=10, command=p1.lift)
        b2 = tk.Button(buttonframe, text="Step 2",font="-family {Segoe UI} -size 13", height=1, width=10, command=p2.lift)
        b3 = tk.Button(buttonframe, text="Step 3",font="-family {Segoe UI} -size 13", height=1, width=10, command=p3.lift)
        # Den här knappen borde se till att spara värden från page3, get funktionerna längst ner i page3
        b4 = tk.Button(buttonframe, text="Calculate",font="-family {Segoe UI} -size 13", height=1, width=10, command=p4.lift)
        
        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")
        b4.pack(side="left")
        
        p1.show()

def start_View():
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")
    root.mainloop()
    

start_View()
#if __name__ == "__main__":
#    root = tk.Tk()
#    main = MainView(root)
#    main.pack(side="top", fill="both", expand=True)
#    root.wm_geometry("400x400")
#    root.mainloop()