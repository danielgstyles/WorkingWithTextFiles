file = open("exampleText.txt", "r") 
contents = file.read()
#contents = file.readline()
file.close
print(contents)