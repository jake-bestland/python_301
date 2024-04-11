# Create two classes that model a rectangle and a circle.
# The rectangle class should be constructed by length and width
# while the circle class should be constructed by radius.
#
# Write methods in the appropriate class so that you can calculate
# the area of both the rectangle and the circle, the perimeter
# of the rectangle, and the circumference of the circle.
from math import pi
class Rectangle:
    """Models length and width of a rectangle"""
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        """calculates area of the rectangle"""
        return self.length * self.width

    def perimeter(self):
        """calculates perimeter of the rectangle"""
        return (self.length * 2) + (self.width * 2)
    
    def __str__(self):
        return f"(length:{self.length}, width:{self.width})"
    
    def __repr__(self):
        return f"Rectangle(length={self.length}, width={self.width})"


class Circle:
    """Models radius of a circle"""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """calculates area of the circle"""
        return (self.radius **2) * pi

    def circumference(self):
        """calculates circumference of the circle"""
        return 2 * pi * self.radius
    
    def __str__(self):
        return f"radius:{self.radius}"
    
    def __repr__(self):
        return f"Circle(radius={self.radius})"


r = Rectangle(3, 5)
print(r.area())
print(r.perimeter())
c = Circle(5)
print(c.area())
print(c.circumference())