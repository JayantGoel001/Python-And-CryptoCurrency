import os
import json
from datetime import datetime
from prettytable import PrettyTable
from colorama import Fore, Back, Style
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
print("MY PORTFOLIO")
print()

portfolio_val = 0.00
last_updated = 0

table = PrettyTable(['Asset', 'Amount Owned', convert + ' Value', 'Price', '1h', '24h', '7d'])

with open("portfolio.txt") as inp:
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
        quotes = currency["quote"][convert]
        market_cap = quotes["market_cap"]
        hour_change = quotes["percent_change_1h"]
        day_change = quotes["percent_change_24h"]
        week_change = quotes["percent_change_7d"]

        price = quotes["price"]
        value = float(price) * float(amount)

        if hour_change>0:
            hour_change = Back.GREEN + str(hour_change) + '%' + Style.RESET_ALL
        else:
            hour_change = Back.RED + str(hour_change) + '%' + Style.RESET_ALL

        if day_change>0:
            day_change = Back.GREEN + str(day_change) + '%' + Style.RESET_ALL
        else:
            day_change = Back.RED + str(day_change) + '%' + Style.RESET_ALL

        if week_change>0:
            week_change = Back.GREEN + str(week_change) + '%' + Style.RESET_ALL
        else:
            week_change = Back.RED + str(week_change) + '%' + Style.RESET_ALL



        portfolio_val += value

        value_string = "{:,}".format(round(value, 2))
        table.add_row([
            name + "(" + symbol + ")",
            amount,
            'Rs.' + value_string,
            'Rs.' + str(price),
            str(hour_change),
            str(day_change),
            str(week_change)
        ])

print(table)
print()

portfolio_val_string = '{:,}'.format(round(portfolio_val, 2))
x = datetime.timestamp(datetime.strptime(last_updated, "%Y-%m-%dT%H:%M:%S.%fZ"))
last_updated_date = datetime.fromtimestamp(x).strftime('%B %d,%Y at %I:%M%p')

print("Total Portfolio Values : "+Back.GREEN + "Rs." + portfolio_val_string + Style.RESET_ALL)
print()
print("API results last updated on "+last_updated_date)
print()