import json
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

url = 'https://pro-api.coinmarketcap.com/v1/global-metrics/quotes/latest'
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '46461c59-18e8-445d-93aa-0dfb99a9b0e0',
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url)
    results = response.json()

    print(response)
    print(json.dumps(results, sort_keys=True, indent=4))
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)
