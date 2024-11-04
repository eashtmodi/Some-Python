# name=str(input ("enter your name: "))
# age=str(input ("enter your age: "))
# marks=str(input ("enter your marks: "))

# name = name+'\n'
# age = age+'\n'
# marks = marks+'\n'


# file=open('test.txt','w')
# file.write(name)
# file.write(age)
# file.write(marks)
# file.close()

file=open('test.txt','r+')

reader=file.readlines()

for i in range(0,5):
    print(reader[i].replace('\n',''))