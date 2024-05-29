#Que - 8 Write a python program to find the longest words

def find_longest_words(sentence):
    words = sentence.split()
    longest_length = 0
    longest_words = []  # Initializing a list to store the longest word(s)

    for word in words:
        
        if len(word) > longest_length:
            longest_length = len(word)    
            longest_words = word    # Resetting the list with a new longest word
            
        elif len(word) == longest_length:
            longest_words.append(word)  # Adding another word with the same length

    return longest_words

# Taking user input
sentence = input("Enter a sentence: ")
# Calling the function
find_longest_words(sentence)
#printing the function
print("The longest word in the sentence are: ",find_longest_words(sentence))