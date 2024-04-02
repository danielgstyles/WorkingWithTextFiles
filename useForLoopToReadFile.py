file = open("numbers.txt")

sum = 0

for line in file:
    #convert each line in an int
    number = int(line)
    sum += number  #same as sum = sum + number

print(f"Total is {sum}")