
import webbrowser
import page_gui

""" made this block a comment so I could keep the code for
    reference but not have it affect the program. Will delete when finished
#creates document if it does not exist
f = open("summer_page.html", "w")
#writes to the document that was created
f.write("<html> <body> <h1> Stay tuned for our amazing summer sale! </h1> </body> </html>")
#closes connection to document
f.close()
#displays file in new web browser tab
webbrowser.open_new_tab("summer_page.html")
"""

def page_create(self):
    #opens file and overrides existing content
    f = open("summer_page.html", "w")
    #writes new content for page 
    f.write("Testing") #need input from self.field1
    f.close()
    webbrowser.open_new_tab("summer_page.html")
    
    




if __name__ == '__main__':
    pass
