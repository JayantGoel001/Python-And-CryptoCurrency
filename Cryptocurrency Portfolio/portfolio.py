import os
import json
from datetime import datetime
from prettytable import PrettyTable
from colorama import Fore, Back, Style
from requests import Session


def getResult(link):
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '46461c59-18e8-445d-93aa-0dfb99a9b0e0',
    }

    session = Session()
    session.headers.update(headers)

    response = session.get(link)
    results_res = response.json()
    return results_res


convert = 'INR'
url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?convert=" + convert
results = getResult(url)

data = results['data']

ticker_url_pairs = {}

for currency in data:
    symbol = currency['symbol']
    url = currency['id']
    ticker_url_pairs[symbol] = url

print()
print("MY PORTFOLIO")
print()

portfolio_val = 0.00
last_updated = 0

table = PrettyTable(['Asset', 'Amount Owned', convert + ' Value', 'Price', '1h', '24h', '7d'])

with open("portfolio.txt") as inp:
    for line in inp:
        name, amount = line.split()
        ticker = name.upper()
