'''
Write a Python class named Circle constructed by a radius and two 
methods which will compute the area and the perimeter of a circle 
'''
import math

class CIRCLE:
    
    def __init__(self, radius):
        self.radius = radius  # Initialize the radius of the circle

    def area_circle(self):
        # Calculate and print the area of the circle
        print("Area of circle is:", math.pi * self.radius * self.radius)

    def perimeter(self):
        # Calculate and print the perimeter (circumference) 
        print("Perimeter of a circle is:", 2 * math.pi * self.radius)

# Get user input for the radius
radius = int(input("Enter radius: "))

# Create an instance of the CIRCLE class with the given radius
c1 = CIRCLE(radius)

c1.area_circle()  # Display the area of the circle
c1.perimeter()    # Display the perimeter of the circle