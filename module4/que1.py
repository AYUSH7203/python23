# Q = 1 What is File function in python? What is keywords to create and write file.

'''
    In Python, there isn't a specific function named File with a capital "F".
However, the open() function is commonly used to create and interact with files.
It's the primary method for handling files in Python.

    To create and write to a file in Python, you can use the open() function with
specific mode parameters.

Here's an example with comments to explain each step:
'''
#Open a file named 'example.txt' in write ('w') mode.
#If the file doesn't exist, it will be created. If it exists,its content will be overwritten.

file = open('example.txt', 'w')

# Write text into the file using the write() method.
file.write('This is an example text that will be written to the file.')

# It's essential to close the file after writing to ensure all data is saved and resources are released.
file.close()