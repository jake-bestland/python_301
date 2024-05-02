# Revisit one of the previous lab exercises that were challenging for you.
# Write a test suite that checks for the correct functionality of the code.
# Then try to refactor your solution, maybe you can make the code more
# concise or more elegant? Keep checking whether you broke the functionality
# by repeatedly running your test suite against your changes.

import unittest
import revisit_wiki_scrape
class TestWikiscrape(unittest.TestCase):

    def setUp(self):
        self.BASE_URL = "https://en.wikipedia.org/"
        self.url = f"{self.BASE_URL}wiki/Web_scraping"

    def test_get_valid_html_respoinse(self):
        index_page = revisit_wiki_scrape.get_page_content(self.BASE_URL)
        page = revisit_wiki_scrape.get_page_content(self.url)
        self.assertEqual(index_page.status_code, 200)
        self.assertEqual(page.status_code, 200)

    def test_get_html_content_returns_html_string(self):
        index_html = revisit_wiki_scrape.get_html_content(self.BASE_URL)
        html = revisit_wiki_scrape.get_html_content(self.url)
        self.assertIn("<!DOCTYPE html>", index_html)
        self.assertIn("<!DOCTYPE html>", html)

    def test_make_soup_makes_soup(self):
        html = revisit_wiki_scrape.get_html_content(self.url)
        soup = revisit_wiki_scrape.make_soup(html)
        self.assertEqual("<class 'bs4.BeautifulSoup'>", str(type(soup)))

    def test_get_main_body_gets_main_body_soup(self):
        html = revisit_wiki_scrape.get_html_content(self.url)
        soup = revisit_wiki_scrape.make_soup(html)
        main_body = revisit_wiki_scrape.get_main_body(soup)
        self.assertGreater(len(main_body), 0)
        self.assertEqual("<class 'bs4.BeautifulSoup'>", str(type(soup)))

    def test_get_all_links_gets_links_from_main_body(self):
        html = revisit_wiki_scrape.get_html_content(self.url)
        soup = revisit_wiki_scrape.make_soup(html)
        self.assertGreater(len(revisit_wiki_scrape.get_all_links(soup)), 0)

    def test_get_non_nav_links_gets_non_nav_links(self):
        html = revisit_wiki_scrape.get_html_content(self.url)
        soup = revisit_wiki_scrape.make_soup(html)
        self.assertNotIn("#", soup)