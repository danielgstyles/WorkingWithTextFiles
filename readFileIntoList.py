list = []
#Opens the Questions.txt file so it can be read into the program
file1 = open("exampleText.txt", "r") 
#Loads the Questions and Answers from the Questions.txt file into a list caller file1
list = file1.readlines()
#Closes the file. You should always close your files once you are finished with it
file1.close

Len = len(list)

for i in range(0,Len):
    textFromFile = list[i]
    textFromFile = textFromFile.rstrip()
    print(textFromFile)
    userInput = input("Type in what the previous line says.")
    if userInput == textFromFile:
        print("Nice Work")
    else:
        print("Not correct")



