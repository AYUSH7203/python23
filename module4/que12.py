# Que 12- Write a Python program to copy the contents of a file to another file. 

# Open the studentinfo in read mode
with open('studentinfo.txt', 'r') as student_file:
    # Read the contents of the student file
    content = student_file.read()

# Open the destination file in write mode
with open('destination_file.txt', 'w') as destination_file:
    # Write the contents into the destination file
    destination_file.write(content)

print("Contents copied from studentinfo.txt to destination_file.txt")

#read destination_file.txt

with open('destination_file.txt', 'r') as destination_file:
    # Read the contents of the student file
    content = destination_file.read()
    print(content)