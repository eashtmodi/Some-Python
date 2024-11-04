def swapFileData():
    file1=input("Enter file 1:- ")
    file2=input("Enter file 2:- ")

    with open(file1,"r") as a:
        file1Data=a.read()

    with open(file2,"r") as b:
        file2Data=b.read()

    with open(file1,"w") as a:
        a.write(file2Data)

    with open(file2,"w") as b:
        b.write(file1Data)

     

swapFileData()
print("Thanks for Taking Service")
print("You may see results by opening files")
input("Please enter to exit")
