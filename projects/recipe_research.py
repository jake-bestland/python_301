# Use your `Ingredients` class to create a URL to an online search
# that allows to look for recipes for dishes made from the
# available ingredients.

import webbrowser
class Ingredient:
    """Models a food item used as an ingredient"""

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def get_info(self):
        wiki_url = f"https://en.wikipedia.org/wiki/{self.name}"
        webbrowser.open(wiki_url)

    def expire(self):
        """expires the ingredient."""
        print(f"whoops, these {self.name} went bad...")
        self.name = "expired " + self.name

    def __str__(self):
        return f"{self.name} ({self.amount})"
    
    def __repr__(self):
        return f"Ingredient(name={self.name}, amount={self.amount})"
    
    def __add__(self, other):
        """Combines two ingredients."""
        new_name = self.name + other.name
        return Ingredient(name=new_name, amount=1)
    

a = Ingredient("apple", 2)
c = Ingredient("carrot", 7)
a.get_info()
c.get_info()