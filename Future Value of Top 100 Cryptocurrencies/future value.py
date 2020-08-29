import locale
import math
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
global_cap = int(data['quote'][convert]['total_market_cap'])

table = PrettyTable(
    [
        'Name',
        'Ticker',
        '% of total global cap',
        'Current',
        '10.9T(GOLD)',
        '35.2T (Narrow Money)',
        '89.5T(World Stock Markets)',
        '95.7T(Broad Money)',
        '280.6T (Real Estate)',
        '558.5T(Derivatives)'
    ]
)

results_ticker = getResult(ticker_url)
data = results_ticker['data']
for currency in data:
    name = currency['name']
    ticker = currency['symbol']
    percentage_of_global_cap = float(currency['quote'][convert]['market_cap']) / float(global_cap)

    current_price = round(float(currency['quote'][convert]['price']), 2)
    available_supply = float(currency['total_supply'])
    trillion10price = round(10.9 * math.pow(10, 9) * percentage_of_global_cap / available_supply, 2)
    trillion35price = round(35.2 * math.pow(10, 9) * percentage_of_global_cap / available_supply, 2)
    trillion89price = round(89.5 * math.pow(10, 9) * percentage_of_global_cap / available_supply, 2)
    trillion95price = round(95.7 * math.pow(10, 9) * percentage_of_global_cap / available_supply, 2)
    trillion280price = round(280.6 * math.pow(10, 9) * percentage_of_global_cap / available_supply, 2)
    trillion558price = round(558.5 * math.pow(10, 9) * percentage_of_global_cap / available_supply, 2)

    percentage_of_global_cap_string = str(round(percentage_of_global_cap * 100, 2)) + "%"
    currency_price_string = 'Rs.' + str(current_price)
    trillion10price_string = 'Rs.' + locale.format_string('%.2f', trillion10price, True)
    trillion35price_string = 'Rs.' + locale.format_string('%.2f', trillion35price, True)
    trillion89price_string = 'Rs.' + locale.format_string('%.2f', trillion89price, True)
    trillion95price_string = 'Rs.' + locale.format_string('%.2f', trillion95price, True)
    trillion280price_string = 'Rs.' + locale.format_string('%.2f', trillion280price, True)
    trillion558price_string = 'Rs.' + locale.format_string('%.2f', trillion558price, True)

    table.add_row(
        [
            name,
            ticker,
            percentage_of_global_cap_string,
            currency_price_string,
            trillion10price_string,
            trillion35price_string,
            trillion89price_string,
            trillion95price_string,
            trillion280price_string,
            trillion558price_string
        ]
    )

print()
print(table)
print()