import shutil
import os
import datetime
import ctypes
import tkinter
from tkinter.filedialog import askdirectory

import transfer_gui




#allows user to select a directory to pull files from
#IN PROGRESS: need a way to store this directory for future use
def select_input():
    global source
    source = askdirectory() + '\\'
    return source 

#allows user to select a directory to copy files to
#IN PROGRESS: need a way to store this directory for future use
def select_output():
    global destination
    destination = askdirectory() + '\\'
    return destination



#transfers files that were modified in last 24 hours
def check_files():
    #gets list of files in source directory
    fileList = os.listdir(source)

    #iterates through list of files
    for file in fileList:
        #gets full path, including file name
        fullPath = source + file

        #gets mtime of the file in full path
        mtime = os.path.getmtime(fullPath)
        #converts mtime to datetime format
        modtime = datetime.datetime.now() - datetime.timedelta(hours=24)
        #if mod time was sooner than 24 hours ago, moves files
        if modtime > twentyfour:
            shutil.move(fullPath, destination)



""" blocking this chunk as a copy to keep for reference. Will delete if not
needed once program is complete
#set where source of files are
source = r'C:/Users/David/Desktop/python_exercises/file_transfer/Folder_A/'

#set destination path
destination = r'C:/Users/David/Desktop/python_exercises/file_transfer/Folder_B/'

A_files = os.listdir(source)
B_files = os.listdir(destination)



#creates variable that keeps track of hours and minutes
time_check = datetime.datetime.now()
is_time = time_check.strftime("%H%M")

#function that copies files from A to B
def copy_files():
    for i in A_files:
        shutil.copy(source+i, destination)
    

#checks if there are any files in dir A that aren't in dir B
def check_files():
    if A_files != B_files:
        copy_files()   

#when local time is midnight, check_files() will execute
if is_time == "0000":
    check_files()

def check_filesA():
    for f in A_files:
        print(f)

def check_filesB():
    for f in B_files:
        print(f)

"""






