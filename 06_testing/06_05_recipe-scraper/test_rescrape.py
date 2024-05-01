# Write a unittest test suite to test the rescrape module

import unittest
import rescrape


class TestRescrape(unittest.TestCase):

    def setUp(self):
        self.BASE_URL = "https://codingnomads.github.io/recipes/"
        self.url = f"{self.BASE_URL}recipes/6-spicy-cajun-chicken.html"

    # requests can establish a connection and receive a valid response
    def test_get_valid_html_response(self):
        index_page = rescrape.get_page_content(self.BASE_URL)
        self.assertEqual(index_page.status_code, 200)
    # the response contains HTML code
    def test_get_html_content_returns_html_string(self):
        page = rescrape.get_html_content(self.BASE_URL)
        self.assertIn("<!DOCTYPE html", page)

    # the HTML can be successfully converted to a Beautiful Soup object
    def test_make_soup_makes_beautifulsoup(self):
        html = rescrape.get_html_content(self.BASE_URL)
        soup = rescrape.make_soup(html)
        self.assertEqual("<class 'bs4.BeautifulSoup'>", str(type(soup)))

    # can identify all links from the index page
    def test_get_recipe_links_gets_recipe_links(self):
        index_html = rescrape.get_html_content(self.BASE_URL)
        index_soup = rescrape.make_soup(index_html)
        self.assertGreater(len(rescrape.get_recipe_links(index_soup)), 0)

    # can identify the author of a recipe
    def test_get_author_finds_author(self):
        html = rescrape.get_html_content(self.url)
        soup = rescrape.make_soup(html)
        author = rescrape.get_author(soup)
        self.assertNotEqual(len(author), 0)
        self.assertEqual("romietomatoes", author)

    # can get the main recipe text
    def test_get_recipe_gets_recipe_text(self):
        html = rescrape.get_html_content(self.url)
        soup = rescrape.make_soup(html)
        recipe = rescrape.get_recipe(soup)
        self.assertIsInstance(recipe, str)
        self.assertGreater(len(recipe), 0)

if __name__ == "__main__":
    unittest.main()
