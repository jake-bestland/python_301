# Create a `Planet()` class that models attributes and methods of
# a planet object.
# Use the appropriate dunder method to get informative output with `print()`

class Planet():
    
    def __init__(self, name, hr_day, day_year, moon):
        self.name = name
        self.hr_day = hr_day
        self.day_year = day_year
        self.moon = moon
    
    def __str__(self):
        return f"{self.name} takes {self.hr_day} hours to complete one rotation, {self.day_year} days to orbit the sun, and it has {self.moon} moons."
    
    def __repr__(self):
        return f"Planet(name={self.name}, hr_day={self.hr_day}, day_year={self.day_year}, moon={self.moon})"

m = Planet("Mars", 24.6, 687, 2)

print(m)