from unittest import TestCase
from NotABot import SiteParser

class Test(TestCase):
    def test_site_parser(self):
        url="https://www.banki.ru/products/currency/cash/jpy/ufa"
        self.assertEqual((2),SiteParser.Site_parser(url))