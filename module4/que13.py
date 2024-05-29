'''
Exception handling in Python is a way to deal with errors or exceptional situations that
occur during the execution of a program.
Errors in Python can broadly be categorized into two types: syntax errors and exceptions.

1 : Syntax Errors: These errors occur when the Python interpreter encounters code
                   that does not conform to the syntax rules of the language.
                   For instance,missing colons at the end of a conditional statement,
                incorrect indentation,or misspelled keywords are considered syntax errors.
                They are detected by the interpreter during the parsing of code and prevent
                the program from running.
                
2 : Exception : Exception handling in Python allows you to gracefully manage and recover
                from these exceptional situations.
                The try, except, else, finally blocks are used for exception handling:

try: The block of code where an exception might occur is placed inside the try block.

except: If an exception occurs within the try block,
        the code inside the except block is executed. You can specify the type of
        exception to catch or use a general except block to catch all exceptions.
        
else: This block executes if no exceptions occur in the try block.

finally: This block is optional and will be executed whether an exception occurs or not.
        It is often used to perform cleanup activities.
'''

try:
    result = 10 / 0  # This will raise a ZeroDivisionError
    print(result)    # This line won't be executed due to the exception
    
except ZeroDivisionError as e:
    print("Error:", e)  # Handling the ZeroDivisionError
    
else:
    print("No exception occurred")
    
finally:
    print("Finally block always executes")