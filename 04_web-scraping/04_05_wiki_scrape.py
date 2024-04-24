# Write a web scraper that fetches the information from the Wikipedia page
# on Web scraping. Extract all the links on the page and filter them so the
# navigation links are excluded.
# Programmatically follow one of the links that lead to another Wikipedia article,
# extract the text content from that article, and save it to a local text file.
# BONUS TASK: Use RegExp to find all numbers in the text.

# import re
import requests
from bs4 import BeautifulSoup
from pprint import pprint

BASE_URL = "https://en.wikipedia.org"
URL = "https://en.wikipedia.org/wiki/Web_scraping"


page = requests.get(URL)
soup = BeautifulSoup(page.text)


non_nav_link = []
main_body = soup.find("div", class_="mw-body-content")
main_links = main_body.find_all("a")

for link in main_links:
    if 'href' in link.attrs.keys():
        if '#' not in link.attrs['href']:
            non_nav_link.append(link["href"])
# pprint(non_nav_link[0])

# non_nav_link[0]
wiki2url = BASE_URL + non_nav_link[0]

wiki2 = requests.get(wiki2url)
w2soup = BeautifulSoup(wiki2.text)

w2_body = w2soup.find("div", class_="mw-body-content")

# with open("wiki_article.txt", "w") as wiki_article:
#     wiki_article.write(w2_body.text)


with open("wiki_article.txt", "r") as wiki_article:
    wiki2_text = wiki_article.read()


