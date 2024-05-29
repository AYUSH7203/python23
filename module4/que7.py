'''
Que - 7
Write a Python program to read a file line by line store it into a variable. 
'''
# File name
file_name = 'studentinfo.txt'

try:
    # Initialize an empty string to store the file contents
    file_contents = ""

    # Open the file in read ('r') mode
    with open(file_name, 'r') as file:
        # Read the file line by line and append each line to the 'file_contents' variable
        for line in file:
            file_contents += line

    # Display the contents of the file stored in the variable
    print(f"Contents of {file_name} stored in a variable:")
    print(file_contents)

except FileNotFoundError:
    print("File {file_name} not found.")
except Exception as e:
    print("An error occurred:", e)