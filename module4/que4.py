#Que - 4 Write a Python program to read first n lines of a file.

# Open the file in read mode ('r')
file = open('studentinfo.txt', 'r')

n = 3  # Number of lines to read from the beginning

# Read all lines into a list
lines = file.readlines()

# Reading the first n lines
first_n_lines = lines[:n]

# Print each line from the first n lines without an extra newline
for line in first_n_lines:
    print(line.rstrip())

# Close the file after reading
file.close()