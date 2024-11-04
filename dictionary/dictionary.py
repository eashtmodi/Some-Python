name=input("WELCOME, PLEASE ENTER YOUR NAME: ")
welcome="HEY, {} WELCOME TO YOUR FIRST E-DICTIONARY".format(name)
print(welcome)
print(name,"sorry for inconvenience but we are working on more words ")

dictionaryWords={
    "consider":"deem to be",
    "minute":"infinitely or immeasurably small",
    "accord":"concurrence of opinion",
    "evident":"clearly revealed to the mind or the senses or judgment",
    "practice":"a customary way of operation or behavior",
    "intend":"have in mind as a purpose",
    "concern":"something that interests you because it is important",
    "commit":"perform an act, usually with a negative connotation",
    "issue":"some situation or event that is thought about",
    "approach":"move towards"
}
print("till then try key terms: ")
while(1):
    print(dictionaryWords.keys())
    Word=input("Please type the word for which u want meaning: ")
    print(name, "There you go:" )
    print(dictionaryWords[Word])
    
