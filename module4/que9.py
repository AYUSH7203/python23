
#Que - 9 Write a Python program to count the number of lines in a text file. 

# Open the file in read mode ('r')
file = open("studentinfo.txt", 'r')

count = 0  # Initialize a counter to keep track of the number of lines

# Iterate through each line in the file and increment the counter
for line in file:
    count += 1

# Print the number of lines in the file
print("Number of lines in the file: ", count)

file.close()  # Close the file after reading
