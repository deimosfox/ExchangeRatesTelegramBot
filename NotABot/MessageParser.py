from NotABot import KeywordsDict
from NotABot import SiteParser
from pyparsing import *
from NotABot import Logger


def ParsMessage(message):
    s2 = message
    city = 'NULL'
    current = 'NULL'
    for key in KeywordsDict.cities:
        if any(word in s2.lower() for word in KeywordsDict.cities.get(key)):
            city = key

    for key in KeywordsDict.currencies:
        if any(word in s2.lower() for word in KeywordsDict.currencies.get(key)):
            current = key

    if current is not 'NULL' and city is not 'NULL':
        if (city != "cb"):
            a = URLMaker(current, city)
            data = "Курс" + " " + current + " в" + " " + city
            return (1, a, data)
        else:
            date = DataParser(message)
            a, date = URLMaker2(current, city, date)
            data = "По данным центробанка курс на " + date + " " + "равен: "
            return (2, a, data)
    elif current is 'NULL' and city is 'NULL':
        Logger.log.info("City and current were not found")
        return (1, 1, 0)
    elif current is 'NULL':
        Logger.log.info("Current was not found")
        return (1, 3, 0)
    elif city is 'NULL':
        Logger.log.info("City  was not found")
        return (1, 4, 0)


def URLMaker(current, city):
    URL = "https://www.banki.ru/products/currency/cash/" + current + "/" + city + "/"
    return (SiteParser.Site_parser(URL))


def URLMaker2(current, city, date):
    if (date == "/" or int(date[len(date) - 5:len(date) - 1]) <= 2020):
        URL = "https://www.banki.ru/products/currency/" + city + date
        return (SiteParser.Site_parser2(URL, current))
    else:
        return 2, "0";


def DataParser(s):
    data = "/"
    if len(re.findall("\d{2}\.\d{2}\.\d{2,4}", s)) != 0:
        data = data + re.findall("\d{2}\.\d{2}\.\d{2,4}", s)[0] + "/"
    return (data)
