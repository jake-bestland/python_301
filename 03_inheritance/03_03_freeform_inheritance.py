# Build on your freeform exercise from the previous section.
# Create child classes of two of the existing classes. Create a child class
# of one of the child classes so that the hierarchy is at least three levels.
#
# Build these classes out step-by-step like you did in the previous exercises.
# Use your notebook to brainstorm ideas and scribble down ideas.
#
# If you cannot think of a way to build on your freeform exercise,
# you can start with a new class from scratch.
# Try to make up your own example for this exercise, but if you are stuck,
# you could start working on the following:
#
# - A `Vehicle()` parent class, with `Truck()` and `Motorcycle()` child classes.
# - A `Restaurant()` parent class, with `Gourmet()` and `FastFood()` child classes.

class Furniture:
    def __init__(self, material, seats):
        self.material = material
        self.seats = seats

    def __str__(self):
        if self.seats > 1:
            return f"This piece of furniture is made out of {self.material}, and seats {self.seats} people."
        else:
            return f"This piece of furniture is made out of {self.material}, and seats {self.seats} person."

class Stool(Furniture):
    """Models a stool, use inches for seat height"""
    def __init__(self, material, seats, seat_height):
        super().__init__(material, seats)
        self.seat_height = seat_height

    def __str__(self):
        return f"{super().__str__()} It also has a seat height of {self.seat_height} inches"

    def adjust_height(self, amount):
        """adjusts height of seat in inches"""
        self.seat_height += amount


class Couch(Furniture):
    
    def __init__(self, material, seats, length, width):
        super().__init__(material, seats)
        self.length = length
        self.width = width


class Vehicle:
    """Models a Vehicle"""
    def __init__(self, make, model, year, passengers):
        self.make = make
        self.model = model
        self.year = year
        self.passengers = passengers

    def __str__(self):
        return f"{self.make}, {self.model}, ({self.year}), holds {self.passengers} passengers."

class Truck(Vehicle):
    def __init__(self, make, model, year, passengers, engine):
        super().__init__(make, model, year, passengers)
        self.engine = engine

    def __str__(self):
        return f"{super().__str__()}  It also has a {self.engine} engine."

class Semi(Truck):
    def __init__(self, make, model, year, passengers, engine="diesel"):
        super().__init__(make, model, year, passengers, engine)

    def add_sleeper(self):
        """adds a bed to the cabin, allowing one more passenger"""
        self.passengers += 1


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, passengers=1):
        super().__init__(make, model, year, passengers)

s = Stool("leather", 1, 30)
s.adjust_height(-5)
print(s)
st = Semi("Peterbuilt", "Model 520", 2021, 2)
st.add_sleeper()
print(st)
v = Vehicle("Chevrolet", "Express", 2020, 7)
print(v)
m = Motorcycle("Kawasaki", "Z900", 2017)
print(m)