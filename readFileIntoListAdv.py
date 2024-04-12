list = []
#Opens the Questions.txt file so it can be read into the program
file1 = open("readFileIntoListAdv.txt", "r") 
#Loads the Questions and Answers from the Questions.txt file into a list caller file1
list = file1.readlines()
#Closes the file. You should always close your files once you are finished with it
file1.close

Len = len(list)

for i in range(0,Len):
    parts = list[i]
    parts = parts.split(":")

    print("This is the first part from line " + str(i+1) + " of the text file - " + parts[0])
    print("This is the second part from line " + str(i+1) + " of the text file - " + parts[1])



