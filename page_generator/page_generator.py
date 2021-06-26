
from tkinter import *
import webbrowser
import page_gui



def page_create(self):
    
    #opens file and overrides existing content
    f = open("summer_page.html", "w")
    #writes new content for page
    new_text = self.source.get()
    f.write(new_text) #need input from self.field1
    f.close()
    webbrowser.open_new_tab("summer_page.html")
    
    




if __name__ == '__main__':
    pass
