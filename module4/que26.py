'''
Explain Inheritance in Python with an example? What is init? Or What 
Is A Constructor In Python?

->Classes can inherit from other classes.
->__init__ fuction method are automatically call in create a class object.
->Constructor means two or more function name is same but defferent perameter.
'''

# Parent class (superclass)
class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        pass

# Child class (subclass) inheriting from Animal
class Dog(Animal):
    def make_sound(self):
        return "Woof!"

# Child class (subclass) inheriting from Animal
class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Creating instances of the subclasses
dog = Dog("Canine")
cat = Cat("Feline")

# Accessing superclass attributes and methods through subclasses
print(dog.species)  # Accessing the 'species' attribute from the Animal class
print(cat.species)

print(dog.make_sound())  # Using the 'make_sound' method from the Animal class
print(cat.make_sound())