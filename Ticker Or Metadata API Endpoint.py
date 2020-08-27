import json
from requests import Session
import numpy as np

start = 1
limit = 10
ar = list(np.arange(start, start + limit))
ids = ",".join(str(x) for x in ar)

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?id=' + ids

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '46461c59-18e8-445d-93aa-0dfb99a9b0e0',
}

session = Session()
session.headers.update(headers)

response = session.get(url)
results = response.json()

print(json.dumps(results, sort_keys=True, indent=4))

data = results["data"]

for currency in data:
    rank = currency["rank"]
    name = currency["name"]
    symbol = currency["symbol"]

    circulating_supply = int(currency["circulating_supply"])
    total_supply = int(currency["total_supply"])

    quotes = currency["quotes"]["USD"]
    market_cap = quotes["market_cap"]
    hour_change = quotes["percent_change_1h"]
    day_change = quotes["percent_change_24h"]
    week_change = quotes["percent_change_7d"]

    price = quotes["price"]
    volume = quotes["volume_24h"]