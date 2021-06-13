#import tkinter modules
from tkinter import *
import tkinter as tk
from tkinter import messagebox

#import related modules
import tracking_functions
import tracking_gui

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #define config of master frame
        self.master = master
        self.master.minsize(500,365)
        self.master.maxsize(500,365) #makes window unscalable by user
        #window centering
        tracking_functions.center_window(self,500,500)
        self.master.title("Student Records")
        self.master.configure(bg="#F0F0F0")
        #catches if user clicks the 'x' in upper corner of app
        self.master.protocol("WM_DELETE_WINDOW", lambda: tracking_functions.ask_quit(self))
        arg = self.master

        #load in GUI widgets from tracking_gui module
        tracking_gui.load_gui(self)

        #instantiate Tkinter menu dropdown object
        menubar = Menu(self.master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", underline=1,accelerator="Ctrl+Q",command=lambda: tracking_functions.ask_quit(self))
        menubar.add_cascade(label="File", underline=0, menu=filemenu)
        
        self.master.config(menu=menubar, borderwidth='1')





if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
