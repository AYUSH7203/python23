'''
Que - 17
when is the finally block executed
'''

try:
    # Some code that may raise an exception
    print("Try block: No exception here")
except Exception as e:
    print("Exception occurred:", e)
finally:
    print("Finally block: Always executed")
'''
The finally block in this example prints a message saying "
Finally block:Always executed"
'''