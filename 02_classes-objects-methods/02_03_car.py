# The classic OOP example: Write a class to model a car. The class should:
#
# 1. Set the attributes model, year, and max_speed in the `__init__()` method.
# 2. Have a method that increases the `max_speed` of the car by 5 when called.
# 3. Have a method that prints the details of the car.
#
# Create at least two different objects of this `Car()` class and demonstrate
# changing the objects' attributes.


class Car:
    """Models"""

    def __init__(self, model, year, max_speed):
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def turbo(self):
        """adds 5 to max speed"""
        print(f"The max speed of the {self.model} has increased by 5")
        self.max_speed = (5 + self.max_speed)

    def details(self):
        print(f'current car details: Model: "{self.model}", Year: {self.year}, Max speed: {self.max_speed}')

    def __str__(self):
        return f'("{self.model}", {self.year}, {self.max_speed})'
    
    def __repr__(self):
        return f"Car(model={self.model}, year={self.year}, max_speed={self.max_speed})"




c = Car("corvette", 2023, 210)
c.details()
c.turbo()
print(c)

m = Car("malibu", 2010, 140)
print(m)
m.turbo()
m.details()