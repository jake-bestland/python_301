# Build a very basic Pokémon class that allows you to simulate battles
# in a Rock-Paper-Scissors game mechanic, as well as feed your Pokémon.
#
# The class should follow these specifications:
#
# - Each Pokemon should have a `name`, `primary_type`, `max_hp` and `hp`
# - Primary types should be limited to `water`, `fire` and `grass`
# - Implement a `battle()` method based on rock-paper-scissors that
#   decides who wins based only on the `primary_type`:
#       water > fire > grass > water
# - Display messages that explain who won or lost a battle
# - If a Pokemon loses a battle, they lose some of their `hp`
# - If you call the `feed()` method on a Pokemon, they regain some `hp`


class Pokemon:
    def __init__(self, name, primary_type, max_hp):
        self.name = name
        self.primary_type = primary_type
        self.max_hp = max_hp
        self.hp = max_hp

    def __str__(self):
        return f"{self.name}, ({self.primary_type}, {self.hp}/{self.max_hp})"
    
    def __repr__(self):
        return f"Pokemon(name={self.name}, primary_type={self.primary_type}, max_hp={self.max_hp})"
    
    def feed(self, amount):
        self.amount = amount
        if (self.hp + self.amount) < self.max_hp:
            self.hp += self.amount
            print(f"You fed {self.name}.  {self.name} now has {self.hp}/{self.max_hp} HP")
        else:
            self.hp = self.max_hp
            print(f"You have fed {self.name}.  {self.name} if now full and at {self.max_hp} HP.")

    
    def battle(self, other):
        print("Battle:", self.name, "vs", other.name)
        result = self.typewheel(self.primary_type, other.primary_type)
        print(f"{self.name} fought {other.name} and the result is a {result}")
        if result == "loss":
            self.hp -= 10
            print(f"{self.name} lost and now has {self.hp}/{self.max_hp} HP")
        if result == "win":
            other.hp -= 10
            print(f"{other.name} lost and now has {other.hp}/{other.max_hp} HP")
        
    @staticmethod
    def typewheel(type1, type2):
        result = {0: "loss", 1:"win", -1: "tie"}
        game_map = {"water": 0, "fire": 1, "grass": 2}
        wl_matrix = [
            [-1, 1, 0], #water
            [0, -1, 1], #fire
            [1, 0, -1], #grass
        ]
        wl_result = wl_matrix[game_map[type1]][game_map[type2]]
        return result[wl_result]


if __name__ == '__main__':
    charm = Pokemon(name="charmander", primary_type="fire", max_hp=150)
    bulbi = Pokemon(name="bulbasaur", primary_type="grass", max_hp=100)
    squirt = Pokemon("squirtle", "water", 125)
    charm.battle(bulbi)
    bulbi.battle(squirt)
    bulbi.battle(charm)
    bulbi.feed(18)