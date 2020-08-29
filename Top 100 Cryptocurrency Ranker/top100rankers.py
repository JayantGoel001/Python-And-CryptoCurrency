from datetime import datetime
from colorama import Back, Style
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


convert = 'INR'
url = "https://pro-api.coinmarketcap.com/v1/global-metrics/quotes/latest?convert=" + convert
results = getResult(url)

data = results['data']

global_cap = data['quote'][convert]['total_market_cap']
global_cap_string = "{:,}".format(global_cap)

print()
print("Coin Market")
print("The global market cap is Rs." + global_cap_string)
print()
print("1---> Top 100 sorted by rank.")
print("2---> Top 100 sorted by 24 hour change")
print("3---> Top 100 sorted by 24 hour Volume")

print()

choice = input("What is your choice?:")
ticker_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?convert='+convert

if choice == '1':
    ticker_url += ''
if choice == '2':
    ticker_url += '&sort=percent_change_24h'
if choice == '3':
    ticker_url += '&sort=volume_24h'

results = getResult(ticker_url)
data = results['data']
print(results)
table = PrettyTable(['Rank', 'Asset', 'Price', 'Market Cap', 'Volume', '1h', '24h', '7d'])
