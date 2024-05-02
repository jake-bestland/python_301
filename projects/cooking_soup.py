
import webbrowser

class Ingredient:
    """Models a food item used as an ingredient"""

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def use(self, use_amount):
        """Reduces the amount of the ingredient available."""
        self.amount -= use_amount

    def expire(self):
        """expires the ingredient."""
        print(f"whoops, these {self.name} went bad...")
        self.name = "expired " + self.name

    def __str__(self):
        return f"{self.amount} {self.name}"
    
    def __repr__(self):
        return f"Ingredient(name={self.name}, amount={self.amount})"
    
class Spice(Ingredient):
    """Models a spice to flavor your food."""

    def __init__(self, name, amount, taste):
        super().__init__(name, amount)
        self.taste = taste

    def expire(self):
        if self.name == "salt":
            print(f"salt never expires! ask the sea!")
        else:
            print(f"your {self.name} has expired.  It's probably still good.")
        self.name = "old " + self.name

    def grind(self):
        print(f"You now have {self.amount} of ground {self.name}.")

class Vegtable(Ingredient):
    def peel(self):
        print(f"You now have {self.amount} of peeled {self.name}.")
        self.name = "peeled " + {self.name}

class Soup:
    def __init__(self, ingredient_list):
        self.ingredient_list = ingredient_list

    def __str__(self):
        return f"This soup is made up of {self.ingredient_list}"

    def cook(self):
        recipe_list = ""
        for ingredient in self.ingredient_list:
            recipe_list += (ingredient.__str__() + ", ")
        recipe_url = f"https://www.google.com/search?q=soup+recipes+using+{recipe_list}"
        webbrowser.open(recipe_url)

c = Ingredient("carrots", 3)
p = Ingredient("potatoes", 2)
peas = Ingredient("peas", 20)
t = Ingredient("tomatoes", 2)

# print(c)
s = Soup([c, p, peas, t])
print(s)
s.cook()