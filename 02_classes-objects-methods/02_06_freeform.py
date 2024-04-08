# Write a script with three classes that model everyday objects.
# - Each class should have an `__init__()` method that sets at least 3 attributes
# - Include a `__str__()` method in each class that prints out the attributes
#     in a nicely formatted string.
# - Overload the `__add__()` method in one of the classes so that it's possible
#     to add attributes of two instances of that class using the `+` operator.
# - Create at least two instances of each class.
# - Once the objects are created, change some of their attribute values.
#
# Be creative. Have some fun. :)
# Using objects you can model anything you want:
# Animals, paintings, card games, sports teams, trees, people etc...


class Athlete:

    def __init__(self, name, age, position, league):
        self.name = name
        self.age = age
        self.position = position
        self.league = league

    def __str__(self):
        return f"{self.name} ({self.age}), is a {self.position} in the {self.league}"
    
    def __repr__(self):
        return f"Athlete(name={self.name}, age={self.age}, position={self.position}, league={self.league})"
    
class SportTeam:

    def __init__(self, location, name, league):
        self.location = location
        self.name = name
        self.league = league
        
    def __str__(self):
        return f"The {self.location} {self.name} play in the {self.league}"
    
    def __repr__(self):
        return f"SportTeam(location={self.location}, name={self.name}, league={self.league})"
    

class IceCreamFlavor:

    def __init__(self, name, scoops, cone_type):
        self.name = name
        self.scoops = scoops
        self.cone_type = cone_type

    def __add__(self, other):
        """combines two flavors"""
        new_name = self.name + other.name
        new_scoops = self.scoops + other.scoops
        return IceCreamFlavor(name=new_name, scoops=new_scoops, cone_type=self.cone_type)
    
    def __str__(self):
        return f"{self.name}, {self.scoops} scoop(s), in a {self.cone_type} cone."
    


jj = Athlete("Justin Jefferson", 24, "WR", "NFL")
kk = Athlete("Kirill Kaprizov", 26, "LW", "NHL")
vikings = SportTeam("Minnesota", "Vikings", "NFL")
wild = SportTeam("Minnesota", "Wild", "NHL")
sberry = IceCreamFlavor("Strawberry", 2, "waffle")
chcake = IceCreamFlavor("Cheesecake", 2, "waffle")

print(jj)
print(kk)
print(vikings)
print(wild)
print(sberry)
print(chcake)
print(sberry + chcake)