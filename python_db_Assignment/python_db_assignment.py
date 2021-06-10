
import sqlite3

conn = sqlite3.connect('db_python_assignment.db')

with conn:
    cur = conn.cursor()
    #creates table
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        file_ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        file_name TEXT)")
    conn.commit() #commits change to dB
conn.close() #ends connection with dB



fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')



conn = sqlite3.connect('db_python_assignment.db') # connects to dB

for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_files (file_name) VALUES (?)", (x,))
            print(x)
conn.close() #ends connection with dB




            
    

