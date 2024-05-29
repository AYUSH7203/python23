'''
Que - 16
Can one block of except statements handle multiple exception?
'''

try:
    result = 10 / 0  # This will raise a ZeroDivisionError
    value = int('hello')  # This will raise a ValueError
    
except (ZeroDivisionError, ValueError) as e:
    # Handling ZeroDivisionError or ValueError
    print("An error occurred:", e)