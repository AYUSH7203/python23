'''
Write a Python class named Rectangle constructed by a length and 
width and a method which will compute the area of a rectangle '''

class Rectangle:
    # Constructor to initialize the height and width of the rectangle
    def __init__(self, x, y):
        self.height = x  # Assigning the height
        self.width = y   # Assigning the width

    # Method to display the area of the rectangle
    def display(self):
        print("Area of rectangle is:", self.height * self.width)

# Creating an instance of the Rectangle class with height 10 and width 6
r = Rectangle(10, 6)

# Displaying the area of the rectangle
r.display()  # Prints the area of the rectangle