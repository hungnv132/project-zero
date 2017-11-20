import requests
from lxml import html
from datetime import datetime
from core.constants import (CRAWL_SOURCE, OPEN_XPATH, CLOSE_XPATH, HIGH_XPATH,
                            LOW_XPATH, REF_XPATH, VOL_XPATH, FOREIGN_BUY_XPATH,
                            FOREIGN_SELL_XPATH, DATE_XPATH, AGREEMENT_XPATH)


def convert_money(money_in_str):
    money_in_float = float(money_in_str) * 1000
    money_in_int = int(money_in_float)
    return money_in_int


def convert_volume(vol_in_str):
    vol = vol_in_str.replace(',', '')
    return int(vol)


def convert_date(date_in_str):
    return datetime.strptime(date_in_str, '%d-%m-%Y').date()


def find_by_xpath(tree, xpath, type='money'):
    value = tree.xpath(xpath)[0]
    if type == 'money':
        return convert_money(value)
    elif type == 'volume':
        return convert_volume(value)
    elif type == 'date':
        return convert_date(value)


def crawl_data(url=CRAWL_SOURCE, symbol=None):
    if not symbol:
        return {}
    url = url.format(symbol=symbol)
    response = requests.get(url, verify=False)
    tree = html.fromstring(response.content)

    return {
        'date': find_by_xpath(tree, DATE_XPATH, 'date'),
        "ref": find_by_xpath(tree, REF_XPATH),
        "open": find_by_xpath(tree, OPEN_XPATH),
        "close": find_by_xpath(tree, CLOSE_XPATH),
        "high": find_by_xpath(tree, HIGH_XPATH),
        "low": find_by_xpath(tree, LOW_XPATH),
        "agreement": find_by_xpath(tree, AGREEMENT_XPATH, 'volume'),
        "foreign_buy": find_by_xpath(tree, FOREIGN_BUY_XPATH, 'volume'),
        "foreign_sell": find_by_xpath(tree, FOREIGN_SELL_XPATH, 'volume'),
        "vol": find_by_xpath(tree, VOL_XPATH, 'volume'),

    }

if __name__ == '__main__':
    print(crawl_data(symbol='fsfsd'))
