#Que -5 Write a Python program to read last n lines of a file

# Open the file in read mode ('r')
file = open('studentinfo.txt', 'r')

n = 3  # Number of lines to read

# Read all lines into a list
lines = file.readlines()

# Reading the last n lines
last_n_lines = lines[n:]

# Print each line from the last n lines without an extra newline
for line in last_n_lines:
    print(line.rstrip())

# Close the file after reading
file.close()