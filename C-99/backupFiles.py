import os 
import shutil

#  taking input
source=input("Please input the folder to backup")
destination=input("Please enter ur destination of backup")

source=source+"/"
destination=destination+"/"

_list_of_files=os.listdir(source)
for files in _list_of_files:
    shutil.copy((source+files),destination)
input("Enter To Exit")
