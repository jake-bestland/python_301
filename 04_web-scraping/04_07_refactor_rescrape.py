# Refactor your web scraping script and wrap all the functionality into
# separate functions. This is a great exercise to revisit writing functions
# as well as for refactoring your code. It'll also help you in an upcoming
# section of the course when you'll write tests for your web scraper.

import requests
from bs4 import BeautifulSoup
from pprint import pprint

BASE_URL = "https://en.wikipedia.org"
URL = "https://en.wikipedia.org/wiki/Web_scraping"

def get_page_content(url):
    """Gets the response from a HTTP call to the URL."""
    page = requests.get(url)
    return page

def get_html_content(url):
    """Gets the HTML from a page."""
    html = get_page_content(url).text
    return html

def make_soup(html):
    """Converts an HTML string to a BeautifulSoup object."""
    soup = BeautifulSoup(html, "html.parser")
    return soup

def get_main_body(soup):
    """Gets the main body content of the wiki page"""
    main_body = soup.find("div", class_="mw-body-content")
    return main_body

def get_all_links(soup):
    """Gets all the links from the given a bs4 object"""
    main_links = soup.find_all("a")
    return main_links

def get_non_nav_links(list, soup):
    """Filters out navigation links from a bs4 object of url links.  The 'list' parameter is the destination for the non navigation links and is what is returned."""
    list = []
    for link in soup:
        if '#' not in link.attrs['href']:
            list.append(link["href"])
    return list



if __name__ == "__main__":
    html = get_html_content(URL)
    soup = make_soup(html)

    non_nav_link = []
    main_body = get_main_body(soup)
    main_links = get_all_links(main_body)
    all_nnl = get_non_nav_links(non_nav_link, main_links)

    pprint(all_nnl)