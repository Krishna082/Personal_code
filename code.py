
###Instatiating a class object
class A(object):

    variable = "String value"  # class variable, value common for all instances of this class
    __private_variable = "Special or 'private' variable with value common for all instances of this class"

    def __new__(cls):
        # cls is the current class
        print("Creating instance")
        return super(A, cls).__new__(cls)

    def __init__(self):
        # self is the current instance
        self.instance_variable = "some value"  # Only the current instance has this value
        print("Init is called")

    def normal_method(self, value):
        """
        Normal method
        :return:
        """
        self.instance_variable = value
        some_variable = "some value"  # local variable only visible in current scope (method)
        return some_variable


A()

### Variable overridden and Object Instatiation

class PatternClass1(object):

    __variable = None  # classes

    def __new__(cls):
        if cls.__variable is None:
            cls.__variable = super(PatternClass1, cls).__new__(cls)
        return cls.__variable


a = PatternClass1()
a.variable = 1
b = PatternClass1()
b.variable = 2


print(a.variable)


### class Inheritance

import abc
class Shape():

    @abc.abstractmethod
    def area(self):
        pass

    @abc.abstractmethod
    def circumference(self):
        pass


class Rectangle(Shape):
    def __init__(self, width=0, length=0):  # 1 if not specified
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length

    def circumference(self):
        return 2 * self.width + 2 * self.length



class Square(Rectangle):
    def __init__(self, length=0):
        super(Square, self).__init__(length, length)


class Circle(Shape):
    def __init__(self, radius=0):
        self.radius = radius

    def area(self):
        return 3.14*self.radius*self.radius

    def circumference(self):
        return 2.0*3.14*self.radius


class FactoryPattern:
    def creatingThreeShapes(self, shape_name):
        if shape_name == 'Rectangle':
            print("The shape created: Rectangle}")
            width = float(input("Please enter width of Rectangle: "))
            length = float(input("Please enter length of Rectangle: "))
            return Rectangle(width, length)
        
        elif shape_name == 'Square':
            print("The shape created: Square")
            length = float(input("To Calculate area and circumference,Please enter length of Square: "))
            return Square(length)

        elif shape_name == 'Circle':
            print("The shape created: Circle")
            radius = float(input("To Calculate area and circumference,Please enter radius of Circle: "))
            return Circle(radius)

# this is genral code for any of the three shapes
def CreatingInstanceShapes(name_of_the_shape):
    factory_pattern = FactoryPattern()
    shape = factory_pattern.creatingThreeShapes(name_of_the_shape)
 
    print("The area of", name_of_the_shape," is ", shape.area())
    print("The circumference of", name_of_the_shape," is ",shape.circumference())
    
# creating instances for circle and Square    
CreatingInstanceShapes("Circle")
CreatingInstanceShapes("Square")

### Calculating sqaures faster with memorizing the values

from time import sleep
from random import random

def time_consuming_square(input):
    sleep(1)  # Do not remove this
    return input * input

class NeedsImprovement(object):
    # memorization helps to run the code faster when calculating squares next time
    def find_square(self, value, value_dict):
        
        if value in value_dict:
            return value_dict[value]
        else:
            value_dict[value] = time_consuming_square(value)
            return time_consuming_square(value)

if __name__ == "__main__":

    value_dict={}

    square_finder = NeedsImprovement() 
    for i in range(1000):
        value = int(10*random()) + 1
        print(square_finder.find_square(value, value_dict))




