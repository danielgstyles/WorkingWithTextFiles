file = open("appendToFile.txt", "a") 
userInput = input("Enter some text to save to a file: ")
file.write(userInput + "\n")
file.close
