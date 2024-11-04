import os
import shutil

path=input("Tell the path of the file")
list_of_file=os.listdir(path)

for fileRead in list_of_file:
    name,ext=os.path.splitext(fileRead)
    ext=ext[1:]
    if ext==" ":
        continue
    if os.path.exists(path+"/"+ext):
        shutil.move(path+"/"+fileRead,path+"/"+ext+"/"+fileRead)
    else:
        os.makedirs(path+"/"+ext)
        shutil.move(path+"/"+fileRead,path+"/"+ext+"/"+fileRead)
input("Enter To Exit")