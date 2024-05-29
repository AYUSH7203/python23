#Que - 2 Write a Python program to read an entire text file.

# Writing student information to a file
file = open("studentinfo.txt", 'w')

# Loop to take input and write to the file
for i in range(1, 3):
    ID = int(input("Enter ID: "))
    NAME = input("Enter Name: ")
    Roll_no = int(input("Enter Roll Number: "))
    file.write(f"\nStudent info: {ID} {NAME} {Roll_no}")

file.close()  # Close the file after writing

# Reading the content from the file and printing it
file_path = 'studentinfo.txt'  # Replace this with the path to your text file
file = open(file_path, 'r')  # Open the file in read mode
content = file.read()  # Read the entire content
print(content)  # Print the content
file.close()  # Close the file after reading