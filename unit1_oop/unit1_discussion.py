"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable. X
# - Include at least two instance variables. X
# - Include a constructor (__init__). X
# - Include a method that returns or displays information about the object. X
#
# Replace the pass statement with your implementation.

class Car:
    #constructor
    def __init__(self, make, model):
        self.make = make
        self.model = model

    #variable
    tires_count = 4

    #method
    def display_car_details(self):
        print("\nMake", self.make, "\nModel", self.model, "\nNumber Of Tires", self.tires_count)

# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance. X
# - Add at least one new class variable. X
# - Add at least two new instance variables. X
# - Add at least one new method. X
# - Override a method from the parent class. X
#
# Replace the pass statement with your implementation.

class GasCar(Car): #inheritance
    #constructor
    def __init__(self, make, model, mpg, color):
        super().__init__(make, model) #inheritance

        #new instance variables
        self.mpg = mpg
        self.color = color

    #new method
    def replace_battery(self):
        print("Battery needs to be replaced soon for", self.make, self.model)

    #new class variable
    motor_type = "Gas"

    #override parent method
    def display_car_details(self):
        print("\nMake:", self.make, "\nModel", self.model, "\nNumber Of Tires", self.tires_count, "\nMotor Type", self.motor_type, "\nMPG", self.mpg, "\nColor", self.color)

# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class. X
# - Access a class variable through the class itself. X
# - Access the same class variable through an object. X
# - Add a new attribute to only one object after it is created. X
# - Display each object's namespace using __dict__. X
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")
    print("TODO: Implement namespace demonstration")

    #2 child class object
    c1 = GasCar("BMW", "328i", 32, "Black")
    c2 = GasCar("Ford", "Mustang", 12, "Red")

    #access class variable via it's class
    print("\nClass variable for number of tires:", GasCar.tires_count)

    #access class variable via object
    print("\nc1 class variable via object for MPG:", c1.mpg)

    #add (update) attribute to one of the new objects
    print("\nc1 class variable update. Was", c1.color)
    c1.color = "Blue"
    print("...but now is", c1.color)

    #display object namespace using "__dict__"
    print("\nc1 namespace:")
    print(c1.__dict__)

    print("\nc2 namespace:")
    print(c2.__dict__)

    #display information about the class namespace
    print("\nGasCar class namespace:")
    print(GasCar.__dict__)

# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data. X
# - Create a shallow copy. X
# - Create a deep copy. X
# - Modify the original object's nested data. X
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")
    print("TODO: Implement shallow copy and deep copy demonstration")

    #object with mutable data
    c3 = GasCar("Dodge", "Dart", 4.7, "Brown")
    c3.info = {
        "top_type": ["Cloth", "Convertable"],
        "radio": ["8 Track Player", "Cassette Player"]
        }

    #shallow copy
    c3_shallow = copy(c3)

    #deep copy
    c3_deep_copy = deepcopy(c3)

    #modify object's nested data
    c3.info["radio"].append("CD Player")

    #display original object, shallow copy, and deep copy
    print("\nOriginal", c3.__dict__)
    print("\nShallow Copy", c3_shallow.__dict__)
    print("\nDeep Copy", c3_deep_copy.__dict__)


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class. X
# - Create at least one object from the child class. X
# - Demonstrate inheritance by calling methods. X
# - Call your namespace demonstration function. X
# - Call your copy demonstration function. X

def main():
    print("=== Unit 1 OOP Assignment ===")
    print("\nTODO: Create and test your parent object")
    print("\nTODO: Create and test your child object")

    #new object from parent class
    c4 = Car("Chevy", "Nova")

    #new object from subclass
    c5 = GasCar("Chevy", "Camero Z28", 1.5, "Brown")

    #inheritance methods from above
    c4.display_car_details()
    c5.display_car_details()
    c5.replace_battery()

    #demo namespace function
    demonstrate_namespaces()

    #demo copy function
    demonstrate_copying()

if __name__ == "__main__":
    main()