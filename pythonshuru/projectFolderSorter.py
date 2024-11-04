import os 
import shutil 

path=input("Tell which folder to sort: ")

files= os.listdir(path)

for i in files:
    fileName,file_extension=os.path.splitext(i)
    file_extension=file_extension[1:]
    if os.path.exists(path+"/"+file_extension):
        shutil.move(path+"/"+i,path+"/"+file_extension)
    else:
        os.mkdir(path+"/"+file_extension)
        shutil.move(path+"/"+i,path+"/"+file_extension)
