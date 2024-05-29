#Que - 10 Write a Python program to count the frequency of words in a file. 
# File name
file_name = 'example.txt'

try:
    # Open the file in read ('r') mode
    with open(file_name, 'r') as file:
        # Read the entire file content
        content = file.read()
        
        # Split the content into words by whitespace
        words = content.split()

        # Create an empty dictionary to store word frequencies
        word_freq = {}

        # Count the frequency of each word
        for word in words:
            # Remove punctuation and convert to lowercase for consistency
            word = word.strip('.,!?').lower()
            if word not in word_freq:
                word_freq[word] = 1
            else:
                word_freq[word] += 1

        # Display the word frequencies
        print("Word frequencies in '{}'".format(file_name))
        for word, freq in word_freq.items():
            print(f"{word}: {freq}")

except FileNotFoundError:
    print("File '{}' not found.".format(file_name))
except Exception as e:
    print("An error occurred:", e)