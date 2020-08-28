from datetime import datetime
import time
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
print("ALERTS TRACKING....")

already_hit_symbol = []

while True:
    with open("alerts.txt") as inp:
        for line in inp:
            ticker, amount = line.split()
            ticker = ticker.upper()

            ticker_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?id=' + str(
                ticker_url_pairs[ticker]) + "&convert=" + convert

            results_ticker = getResult(ticker_url)

            currency = results_ticker['data'][str(ticker_url_pairs[ticker])]

            rank = currency["cmc_rank"]
            name = currency["name"]
            symbol = currency["symbol"]
            last_updated = currency["last_updated"]