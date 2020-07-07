from unittest import TestCase
from NotABot import MessageParser


class Test(TestCase):
    def test_full_wrong_input(self):
        message = 'pishi message'
        self.assertEqual((1, 1, 0), MessageParser.ParsMessage(message))

    def test_city_only(self):
        message = 'pishi message в москве'
        self.assertEqual((1, 3, 0), MessageParser.ParsMessage(message))

    def test_current_only(self):
        message = 'pishi message в долларе'
        self.assertEqual((1, 4, 0), MessageParser.ParsMessage(message))

    def test_url_maker_2(self):
        current = 'usd'
        city = 'cb'
        date = "14.05.2022/"
        self.assertEqual(( 2,"0"), MessageParser.URLMaker2(current,city,date))
