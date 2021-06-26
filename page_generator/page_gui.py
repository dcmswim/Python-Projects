import tkinter as tk
from tkinter import *
from tkinter import ttk

import page_generator


class main_window(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.pack()
        self.master.title("Page Generator")
        self.inputlabel = tk.Label(self, text = "Input body text:")
        self.inputlabel.grid(row = 0, column = 0, sticky = tk.W, padx = 10)

        self.source = StringVar()
        self.field1 = tk.Entry(self, textvariable = self.source)
        self.field1.grid(row = 0, column = 2, columnspan = 5, padx = 10)

        self.button1 = Button(self, text = "Close program")
        self.button1.grid(row = 6, column = 0, sticky = tk.W, padx = 10, pady = 10,)
        self.button2 = Button(self, text = "Submit", command = lambda: page_generator.page_create(self))
        self.button2.grid(row = 6, column = 6, sticky = tk.E, padx = 10)
       


def main():
    main_window().mainloop()






if __name__ == '__main__':
    main()
