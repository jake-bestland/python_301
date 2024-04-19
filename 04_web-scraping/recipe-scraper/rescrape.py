# For this project, your task is to create a CLI that takes as an input
# the names of ingredients from a user. Then, your code will fetch
# the recipe information from the CodingNomads recipe collection,
# and search through the text of the recipes to find ones that include
# the provided ingredients.
#
# Note: Feel free to integrate your custom Ingredient() and Soup() classes
# into the code base, to get some additional practice in working with your
# custom Python classes.

# from projects.cooking_soup import Ingredient, Soup
import requests
from bs4 import BeautifulSoup
from pprint import pprint

URL = "https://codingnomads.github.io/recipes/"
page = requests.get(URL)
soup = BeautifulSoup(page.text)

link_url = [URL + link["href"] for link in soup.find_all("a")]

### take names of ingredients as input from user
ingredients = input("Please enter the ingredients you would like to use: ").split(', ')

### fetch recipe link using provided ingredients.  ## all ingredients must be in recipe
recipes = []
check_list = []
for r_link in link_url:
    r_page = requests.get(r_link)
    r_soup = BeautifulSoup(r_page.text)
    rec_ingred = r_soup.find("div", class_="md")
    for i in ingredients:
        if i in rec_ingred.text:
            check_list.append(i)
    if check_list == ingredients:
        recipes.append(r_link)
    else:
        check_list.clear()


pprint(recipes)