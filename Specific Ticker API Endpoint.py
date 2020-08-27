import json
from requests import Session


def getResult(url):
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '46461c59-18e8-445d-93aa-0dfb99a9b0e0',
    }

    session = Session()
    session.headers.update(headers)

    response = session.get(url)
    results = response.json()
    return results


url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

result = getResult(url)
print(json.dumps(result, sort_keys=True, indent=4))

data = result['data']

ticker_url_pairs = {}

for currency in data:
    symbol = currency['symbol']
    url = currency['id']
    ticker_url_pairs[symbol] = url

print(ticker_url_pairs)

choice = input("Enter the ticker symbol of a cryptocurrency:")
choice = choice.upper()
ticker_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?id=' + str(ticker_url_pairs[choice])
result_ticker = getResult(ticker_url)
print(json.dumps(result_ticker, sort_keys=True, indent=4))
