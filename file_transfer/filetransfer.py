import shutil
import os
import datetime

#set where source of files are
source = r'C:/Users/David/Desktop/python_exercises/file_transfer/Folder_A/'

#set destination path
destination = r'C:/Users/David/Desktop/python_exercises/file_transfer/Folder_B/'

A_files = os.listdir(source)
B_files = os.listdir(destination)



#function that copies files from A to B
def copy_files():
    for i in A_files:
        shutil.copy(source+i, destination)

#checks if there are any files in dir A that aren't in dir B
def check_files():
    if A_files != B_files:
        copy_files()



#Constantly checks current time as long as X is true
X = True
while X is True:
    def get_time():
        time_check = datetime.datetime.now()
        #creates variable that keeps track of hours and minutes
        is_time = time_check.strftime("%H%M")
        #when local time is midnight, check_files() will execute
        if is_time == "0000":
            check_files()








