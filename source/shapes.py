import math


class Shapes: #Class Based Test

    def __init__(self):
        pass

    def parameter(self):
        pass


class Circle(Shapes):


    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (math.pi) * (self.radius**2)
    
    def perimeter(self):
        return  2 * math.pi * self.radius

class Rectangle(Shapes):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return (self.length * 2) + (self.width * 2)