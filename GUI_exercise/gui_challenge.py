import tkinter as tk
from tkinter import *
from tkinter import ttk

import file_dialog


class main_window(Frame):
    def __init__(self):
        Frame.__init__(self)

        
        
        self.pack()
        self.master.title("Check files")
        self.button1 = Button(self, text = "Browse", command = file_dialog.callback)
        self.button1.grid(row = 0, column = 0, sticky = tk.W, padx = 10, pady = 10)
        self.button2 = Button(self, text = "Browse", command = file_dialog.callback)
        self.button2.grid(row = 1, column = 0, sticky = tk.W, padx = 10, pady = 10)
        self.button3 = Button(self, text = "Check for files")
        self.button3.grid(row = 2, column = 0, sticky = tk.W, padx = 10, pady = 10,)
        self.button4 = Button(self, text = "Close program")
        self.button4.grid(row = 2, column = 6, sticky = tk.E, padx = 10)
        field1 = tk.Entry(self)
        field1.grid(row = 0, column = 2, columnspan = 5, padx = 10)
        field2 = tk.Entry(self)
        field2.grid(row = 1, column = 2, columnspan = 5, padx = 10)


def main():
    main_window().mainloop()






if __name__ == '__main__':
    main()
            
        
