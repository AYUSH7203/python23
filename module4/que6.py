#Que - 6 Write a Python program to read a file line by line and store it into a list

# File name
file_name = 'studentinfo.txt'

try:
    # Open the file in read ('r') mode
    file = open(file_name, 'r')

    ''' Iterate through each line in the file and
    print it after removing leading/trailing whitespace'''
    for line in file.readlines():
        print(line.strip())

    # Close the file after reading its contents
    file.close()

except FileNotFoundError:
    print("File not found. Please provide the correct file.")

except Exception as e:
    print("An error occurred:", e)
