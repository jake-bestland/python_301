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

article = soup.article
for section in article.find_all("section", class_="step"):
    pprint(section.text)