import json
from requests import Session

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'API_KEY',
}

session = Session()
session.headers.update(headers)

response = session.get(url)
results = response.json()

print(json.dumps(results, sort_keys=True, indent=4))

data = results["data"]

for currency in data:
    rank = currency["id"]
    name = currency["name"]
    symbol = currency["symbol"]

    print(str(rank)+" : "+name+" ("+symbol+")")
