import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askdirectory

import filetransfer


class main_window(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.pack()
        self.master.title("File Transfer")
        self.buttonA = tk.Button(self, text = "Browse for input directory", command = lambda:filetransfer.select_input(self))
        self.buttonA.grid(row = 0, column = 0, sticky = tk.W, padx = 10)
        self.fieldA = tk.Entry(self) #this will be where input dir will be specified
        self.fieldA.grid(row = 0, column = 1, columnspan = 5, padx = 10)
        self.buttonB = tk.Button(self, text = "Browse for output directory", command = lambda:filetransfer.select_output(self))
        self.buttonB.grid(row = 1, column = 0, padx = 10)
        self.fieldB = tk.Entry(self) #this is where output dir will be specified
        self.fieldB.grid(row = 1, column = 1, columnspan = 5, padx = 10)

        self.button1 = Button(self, text = "Manually transfer files", command = lambda:filetransfer.check_files(self))
        self.button1.grid(row = 6, column = 0, sticky = tk.W, padx = 10, pady = 10)
        
       


def main():
    main_window().mainloop()






if __name__ == '__main__':
    main()
