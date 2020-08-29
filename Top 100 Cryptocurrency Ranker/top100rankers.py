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
ticker_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?convert=' + convert

if choice == '1':
    ticker_url += ''
if choice == '2':
    ticker_url += '&sort=percent_change_24h'
if choice == '3':
    ticker_url += '&sort=volume_24h'

results = getResult(ticker_url)
data = results['data']

table = PrettyTable(['Rank', 'Asset', 'Price', 'Market Cap', 'Volume', '1h', '24h', '7d'])
for currency in data:
    rank = currency["cmc_rank"]
    name = currency["name"]
    symbol = currency["symbol"]
    last_updated = currency["last_updated"]
    quotes = currency["quote"][convert]
    market_cap = quotes["market_cap"]
    hour_change = quotes["percent_change_1h"]
    day_change = quotes["percent_change_24h"]
    week_change = quotes["percent_change_7d"]

    price = quotes["price"]
    volume = quotes['volume_24h']

    if hour_change is not None and hour_change > 0:
        hour_change = Back.GREEN + str(hour_change) + '%' + Style.RESET_ALL
    else:
        hour_change = Back.RED + str(hour_change) + '%' + Style.RESET_ALL

    if day_change is not None and day_change > 0:
        day_change = Back.GREEN + str(day_change) + '%' + Style.RESET_ALL
    else:
        day_change = Back.RED + str(day_change) + '%' + Style.RESET_ALL

    if week_change is not None and week_change > 0:
        week_change = Back.GREEN + str(week_change) + '%' + Style.RESET_ALL
    else:
        week_change = Back.RED + str(week_change) + '%' + Style.RESET_ALL

    if volume is not None:
        volume_string = "{:,}".format(volume)

    if market_cap is not None:
        market_cap = "{:,}".format(market_cap)

    table.add_row(
        [
            rank,
            name + '(' + symbol + ')',
            'Rs.' + str(price),
            'Rs.' + str(market_cap),
            'Rs.' + volume_string,
            str(hour_change),
            str(day_change),
            str(week_change)
        ]
    )

print()
print(table)
print()
