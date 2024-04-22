# Look for a static website online that has some information that you're
# interested in. Follow the web-scraping steps described in the course to
# inspect, scrape, and parse the information.
# BE RESPECTFUL! Don't scrape sites that don't want to be scraped, and
# limit the amount of calls you make to their page by saving the response
# to a file, and parsing the content from that file.

import json
import requests
from bs4 import BeautifulSoup
from pprint import pprint
URL = "https://www.instructables.com/How-to-Play-Phase-10/"

page = requests.get(URL)
soup = BeautifulSoup(page.text)

# article = soup.article
# rules = ""
# for section in article.find_all("section", class_="step"):
#     rules += f"\n{section.text}\n"

# print(rules)

# with open("phase_10_rules.txt", "w") as p10_rules:
#     p10_rules.write(rules)


with open("phase_10_rules.txt", "r") as p10_rules:
    rules = p10_rules.read()

print(rules)