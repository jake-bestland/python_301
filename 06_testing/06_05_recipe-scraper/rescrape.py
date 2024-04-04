import requests
from bs4 import BeautifulSoup


BASE_URL = "https://codingnomads.github.io/recipes/"

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

def get_recipe_links(soup):
    """Extracts the URLs of all links on a page, given a bs4 object."""
    links = [link["href"] for link in soup.find_all("a")]
    return links

def get_author(soup):
    """Extracts the name of the author of a recipe."""
    author = soup.find("p", class_="author").text.strip("by ")
    return author

def get_recipe(soup):
    """Extracts the recipe text from a bs4 object."""
    recipe = soup.find("div", class_="md").text
    return recipe

# breakpoint()

if __name__ == "__main__":
    index_html = get_html_content(BASE_URL)
    index_soup = make_soup(index_html)
    recipe_links = get_recipe_links(index_soup)
    # breakpoint()

    for r_link in recipe_links:
        URL = f"{BASE_URL}/{r_link}"
        soup = make_soup(get_html_content(URL))
        # breakpoint()
        author = get_author(soup)
        recipe = get_recipe(soup)
        print(f"({author})\t[{recipe}]\n\n\n")
