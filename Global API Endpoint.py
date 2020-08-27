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

    active_currency = results["data"]["active_cryptocurrencies"]
    active_markets = results["data"]["active_market_pairs"]
    bitcoin_percentage = results["data"]["btc_dominance"]
    last_updates = results["data"]["last_updated"]
    global_cap = results["data"]["quote"]["USD"]["total_market_cap"]
    global_volume = results["data"]["quote"]["USD"]["total_volume_24h"]

    print("Active Currency :", active_currency)
    print("Active Market :", active_markets)
    print("Bitcoin Percentage :", bitcoin_percentage)
    print("Last Updated :", last_updates)
    print("Global Capital :", global_cap)
    print("Global volume :", global_volume)

except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)
