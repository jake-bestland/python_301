# Research for interesting APIs online and pick two. You can also use APIs that
# you've already worked with in the course if you prefer.
# Write a program that makes calls to both APIs and find a way to combine the
# data that you receive from both of them.
# E.g.: You could use the Ghibli API to find all ghosts from their films, and
#       create an opposing team of Ghost Pokémon from the Poke API.
import json
import requests
from pprint import pprint

GHIBLI_BASE_URL = "https://ghibliapi-iansedano.vercel.app"
response = requests.get("https://ghibliapi-iansedano.vercel.app/api/species")
# data = response.json()

# with open("species.json", "w") as fout:
#     json.dump(data, fout)

with open("species.json", "r") as fin:
    data = json.load(fin)

species = data['data']['species']
ghibli_ghost = ""

for type1 in species:
    if type1['name'] == "Spirit":
        ghibli_ghost += str(type1['people'])

gg_page = requests.get(ghibli_ghost.strip("[']"))
# gg_data = gg_page.json()

# with open("ghibli_ghost.json", "w") as g_g:
#     json.dump(gg_data, g_g)
        
with open("ghibli_ghost.json", "r") as g_g:
    gg_data = json.load(g_g)

spirit_of_ghibli = (gg_data['data'][0]).get('name')


POKE_BASE_URL = "https://pokeapi.co/api/v2/"
        
poke_page =requests.get(POKE_BASE_URL + "type/8")
# poke_data = poke_page.json()

# with open("poke_ghost_types.json", "w") as ghost_types:
#     json.dump(poke_data, ghost_types)

with open("poke_ghost_types.json", "r") as ghost_types:
    ghost_data = json.load(ghost_types)


ghost1 = (ghost_data['pokemon'][0]['pokemon']).get("name")
ghost2 = (ghost_data['pokemon'][1]['pokemon']).get("name")

print(f"There is going to be a battle between the spirit of ghibli: {spirit_of_ghibli}, and the pokemon: {ghost1.capitalize()}, and {ghost2.capitalize()}!")