# Que - 11 Write a Python program to write a list to a file. 
 
file_name = 'example.txt'
li1 = [1,2,3,4,5]

with open(file_name,'w') as file:
    for item in li1:
        file.write(str(item) + '\n')

file = open(file_name, 'r') 
content = file.read()  # Read the entire content
print(content)