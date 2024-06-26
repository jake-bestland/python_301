# Read through the documentation of the Ghibli API and reproduce the example
# listed at https://ghibliapi.herokuapp.com/#section/Use-Case in Python.
# Try skim the Haskell code example and see if you can understand anything.
# Don't worry if you don't, it's a completely different language :)
#
# Your task is to use the API to find information about all the cats that
# appear in Studio Ghibli films.


import json
import requests
from pprint import pprint

BASE_URL = "https://ghibliapi-iansedano.vercel.app"
page = requests.get('https://ghibliapi-iansedano.vercel.app/api/species')
# data = page.json()

# with open("species.json", "w") as fout:
#     json.dump(data, fout)

with open("species.json", "r") as fin:
    data = json.load(fin)

species = data['data']['species']

for type in species:
    if type['name'] == "Cat":
        pprint(type)
        
        

