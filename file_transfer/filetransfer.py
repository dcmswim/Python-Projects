import shutil
import os
import datetime
import ctypes
import tkinter
from tkinter.filedialog import askdirectory


import transfer_gui




#allows user to select a directory to pull files from
#IN PROGRESS: need a way to store this directory for future use
def select_input(self):
    source = askdirectory() + '\\'
    self.fieldA.delete(0)
    self.fieldA.insert(0, source) #need to get this value stored as variable?
     
    

#allows user to select a directory to copy files to
#IN PROGRESS: need a way to store this directory for future use
def select_output(self):
    destination = askdirectory() + '\\'
    self.fieldB.delete(0)
    self.fieldB.insert(0, destination) #need to get this value stored as variable?
    


#transfers files that were modified in last 24 hours
def check_files(self):
    #gets list of files in source directory
    fileList = os.listdir(source)

    #iterates through list of files
    for file in fileList:
        #gets full path, including file name
        fullPath = source + file

        #gets mtime of the file in full path
        mtime = os.path.getmtime(fullPath)
        #converts mtime to datetime format
        modtime = datetime.datetime.fromtimestamp(mtime)
        #creates a variable that holds the time from 24 hrs ago
        twentyfour = datetime.datetime.now() - datetime.timedelta(hours=24)
        #if mod time was sooner than 24 hours ago, moves files
        if modtime > twentyfour:
            shutil.move(fullPath, destination)



if __name__ == '__main__':
    pass






