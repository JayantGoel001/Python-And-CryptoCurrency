import math
import json
import locale
import requests
from prettytable import PrettyTable
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


locale.setlocale(locale.LC_ALL, 'en-US.UTF-8')
convert = 'INR'
global_url = 'https://pro-api.coinmarketcap.com/v1/global-metrics/quotes/latest?convert=' + convert
ticker_url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?convert=" + convert

results = getResult(global_url)
data = results['data']
global_cap = int(data['quote'][convert]['market_cap'])

table = PrettyTable(
    [
        'Name',
        'Ticker',
        '% of total global cap',
        'Current',
        '7.7T(GOLD)',
        '36.8T (Narrow Money)',
        '73T(World Stock Markets)',
        '90.4T(Broad Money)',
        '217T (Real Estate)',
        '544T(Derivatives)'
    ]
)

results_ticker = getResult(ticker_url)
data = results_ticker['data']

