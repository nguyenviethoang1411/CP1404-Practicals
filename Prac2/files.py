OUTPUT_FILE = "name.txt"
file_out = open(OUTPUT_FILE, "w")
name = input("Please Enter your name: ")
print("Your name is: " + str(name), file=file_out)



# program that return the sum of all numbers in numbers.txt
answer = 0
# 1 open the file
file = open("numbers.txt", "r")

# 2, read the file
for line in file:
    answer += (int(line))

# 3, answer the question
print(answer)

# 4 close the file
file.close()
