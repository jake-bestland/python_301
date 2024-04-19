# Use the Pokemon API at https://pokeapi.co/ to assemble a team of your
# six favorite Pokémon.
# Your task is to fetch information about six Pokémon through the
# necessary API calls and include the information in your local script.
# This information should include at least:
# - name
# - number
# - types
#
# You can improve on your project even more by writing the data to a small
# `.html` page which allows you to also display the sprites of each Pokémon.
# Check out the guides they provide: https://pokeapi-how.appspot.com/page5

import requests
import json
from pprint import pprint

BASE_URL = "https://pokeapi.co/api/v2/"

# pika_page = requests.get(BASE_URL + "pokemon/pikachu")
# pika_data = pika_page.json()

# with open("pikachu.json", "w") as pika:
#     json.dump(pika_data, pika)

## repeat above for different pokemon.

with open("pikachu.json", "r") as pika:
    pika_data = json.load(pika)

with open("charizard.json", "r") as char:
    char_data = json.load(char)

with open("squirtle.json", "r") as squirt:
    squirt_data = json.load(squirt)

with open("flareon.json", "r") as flar:
    flar_data = json.load(flar)

with open("bulbasaur.json", "r") as bulb:
    bulb_data = json.load(bulb)

with open("ninetales.json", "r") as nine:
    nine_data = json.load(nine)


    
pika_name = pika_data['name']
pika_num = pika_data['id']
pika_type = [type['type']['name'] for type in pika_data['types']]

char_name = char_data['name']
char_num = char_data['id']
char_type = [type['type']['name'] for type in char_data['types']]

squirt_name = squirt_data['name']
squirt_num = squirt_data['id']
squirt_type = [type['type']['name'] for type in squirt_data['types']]

flar_name = flar_data['name']
flar_num = flar_data['id']
flar_type = [type['type']['name'] for type in flar_data['types']]

bulb_name = bulb_data['name']
bulb_num = bulb_data['id']
bulb_type = [type['type']['name'] for type in bulb_data['types']]

nine_name = nine_data['name']
nine_num = nine_data['id']
nine_type = [type['type']['name'] for type in nine_data['types']]


print(pika_name, pika_num, pika_type)
print(char_name, char_num, char_type)
print(squirt_name, squirt_num, squirt_type)
print(flar_name, flar_num, flar_type)
print(bulb_name, bulb_num, bulb_type)
print(nine_name, nine_num, nine_type)