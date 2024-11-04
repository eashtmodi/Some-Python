import os
# print(os.getcwd())
files= os.listdir()
# print(files)
# for i in files:
#     print(i)
# os.mkdir("ABC")
for i in range(1000):
    os.rmdir(str(i))
