introString=input("enter ur name")
characterCount=0
wordCount=1
for i in introString:
        characterCount=characterCount+1
        if(i==" "):
                wordCount=wordCount+1
print("Number Of words in string")
print(wordCount)
print("Number of character in strings")
print(characterCount)
input ("Enter To Exit")