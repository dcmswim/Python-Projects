import tkinter as tk
from tkinter import filedialog as fd

import gui_challenge

#function for 1st browse button
#gets dir name and populates field with selected dir
def callback(self):
    name = fd.askdirectory()
    self.field1.delete(0)
    self.field1.insert(0, name)

#function for 2st browse button
#gets dir name and populates field with selected dir
def callback2(self):
    name = fd.askdirectory()
    self.field2.delete(0)
    self.field2.insert(0, name)
    
    
    
    





if __name__ == '__main__':
    pass
