
'''
Que - 14
How many except statements can a try-except block have? Name Some 
built-in exception classes:
'''
try:
    # Some code that might raise exceptions
    pass
except ValueError:
    # Handle ValueError
    pass
except TypeError:
    # Handle TypeError
    pass
except ZeroDivisionError:
    # Handle ZeroDivisionError
    pass
# You can have multiple except blocks for different exception types
# More except blocks as needed...

'''

Some of the built-in exception classes in Python include:

ValueError: Raised when a function receives an argument of correct type
            but with an inappropriate value.

TypeError: Raised when an operation or function is applied to an object of inappropriate type.

ZeroDivisionError: Raised when division or modulo operation is performed with zero
                as the divisor.

IndexError: Raised when a sequence subscript is out of range.

KeyError: Raised when a dictionary key is not found.

FileNotFoundError: Raised when a file or directory is requested but cannot be found.

IOError: Raised when an input/output operation fails.

NameError: Raised when a local or global name is not found.

AttributeError: Raised when an attribute reference or assignment fails.

SyntaxError: Raised when there is a syntax error in the code.

'''
