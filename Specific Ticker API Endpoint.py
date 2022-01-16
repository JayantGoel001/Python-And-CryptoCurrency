import json
from requests import Session


def getResult(link):
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'API_KEY',
    }

    session = Session()
    session.headers.update(headers)

    response = session.get(link)
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

currency = result_ticker['data'][str(ticker_url_pairs[choice])]
rank = currency["cmc_rank"]
name = currency["name"]
symbol = currency["symbol"]

circulating_supply = int(currency["circulating_supply"])
total_supply = int(currency["total_supply"])

quotes = currency["quote"]["USD"]
market_cap = quotes["market_cap"]
hour_change = quotes["percent_change_1h"]
day_change = quotes["percent_change_24h"]
week_change = quotes["percent_change_7d"]

price = quotes["price"]
volume = quotes["volume_24h"]

volume_string = "{:,}".format(volume)
market_cap_string = "{:,}".format(market_cap)
circulating_supply_string = "{:,}".format(circulating_supply)
total_supply_string = "{:,}".format(total_supply)

print(str(rank) + " : " + name + "( " + symbol + " ) ")
print('Market Cap :                          $' + market_cap_string)
print('Price :                               $' + str(price))
print('24h Volume :                          $' + volume_string)
print('Hour Change :                         ' + str(hour_change) + '%')
print('Day Change :                          ' + str(day_change) + '%')
print('Week Change :                         ' + str(week_change) + '%')

print("Total Supply :                        " + total_supply_string)
print("Circulating Supply :                  " + total_supply_string)
print("Percentage of coins in circulation :  " + str(round(circulating_supply / total_supply)*100) + "%")
print()
