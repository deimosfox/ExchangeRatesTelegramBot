from selenium import webdriver
from NotABot import Logger

driver = webdriver.Chrome('C:\\chromedriver_win32\\chromedriver.exe')


def Site_parser(URL):
    a = []
    b = []
    driver.get(URL)
    try:
        table = driver.find_element_by_css_selector('body > div.layout-wrapper.padding-top-default.bg-white.position-relative > \
        div.layout-columns-wrapper > main > div.tabs-big > div:nth-child(2) > div:nth-child(1) > section > div > \
        div:nth-child(1) > div > div:nth-child(2)')
    except Exception:
        Logger.log.exception("Error!Sigment is not found")
        return (2)
    else:
        for x in table.get_property('children'):
            if (len(x.get_property('dataset')) != 0):
                a.append([y.get_property('innerText') for y in
                          x.find_elements_by_class_name('table-flex__rate.font-size-large.text-nowrap')][0:2])
                b.append([y.get_property('innerText') for y in x.find_elements_by_class_name('font-bold')][0:1])
        data = []
        for i in range(len(a)):
            data.append((b[i][0], (a[i][0][0:7]), a[i][1]))
        data.sort(key=lambda i: i[1], reverse=1)
        return data


def Site_parser2(URL, current):
    driver.get(URL)
    try:
        table = driver.find_element_by_css_selector('body > div.layout-wrapper.padding-top-default.bg-white.position-relative > div.layout-columns-wrapper > main > \
         div.widget > table > tbody').get_property('children')
        date = driver.find_element_by_css_selector(
            'body > div.layout-wrapper.padding-top-default.bg-white.position-relative > div.layout-columns-wrapper > main > div.widget > header > h2 > span').text
    except Exception:
        Logger.log.exception("Error!Sigment in a currency by date is not found")
        return (2, "0")
    for x in table:
        if x.text.lower()[0:3] == current:
            data = (x.text[0:len(x.text) - 8])
            return (data, date)

    return (2, "0")
