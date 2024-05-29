# Que - 3 Write a Python program to append text to a file and display the text. 

# File name
file_name = 'example.txt'

# Text to be appended
text_to_append = 'This text will be appended to the file.'

try:
    # Open the file in append ('a') mode
    with open(file_name, 'a') as file:
        
        # Append text to the file
        file.write('\n' + text_to_append)

    # Open the file in read ('r') mode to display the appended text
    with open(file_name, 'r') as file:
        
        # Read and display the contents of the file
        file_contents = file.read()
        print("Contents of '{}' after appending:".format(file_name))
        print(file_contents)

except FileNotFoundError:
    print("File '{}' not found.".format(file_name))
except Exception as e:
    print("An error occurred:", e)