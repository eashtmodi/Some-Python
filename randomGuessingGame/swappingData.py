def readingWriting():
    fileName1=input("Enter The name of first file: ")
    fileName2=input("Enter The name of second file please: ")
    print("Thanks Intilazing...")
    file1=open(fileName1,'r+')
    file2=open(fileName2,'r+')
    
    for i in file1:
        file1Data=i
        file2.write(file1Data)
    for x in file2:
        file2Data=x
        file1.write(file2Data)
    
    file1.close()
    file2.close()
    
    
        
        
readingWriting()
print("Thanks for Taking Modi's Service")
print("You may see results by opening files")
input("Please enter to exit")
