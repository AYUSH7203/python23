
'''
Que - 15
When will the else part of try-except-else be executed?
'''

try:
    result = 10 / 1  
    print(result)
    
except ZeroDivisionError as e:
    print("Error:", e)  # Handling the ZeroDivisionError
    
else:
    print("No exception occurred")

'''
    The else block is executed when the code inside the try block runs successfully
    without raising any exceptions.
    If any exception occurs within the try block, the control skips the else block and
    moves directly to the appropriate except block to handle the exception.

    This else block in the try-except-else structure is particularly useful for situations
    where you want to execute some code only if no exceptions are encountered, providing
    a way to separate the code that might raise exceptions from the code that should
    execute only when no exceptions occur.
'''
