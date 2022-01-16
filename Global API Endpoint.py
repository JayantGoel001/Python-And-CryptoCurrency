import json
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from datetime import datetime

countries = ['USD', 'INR']
for country in countries:
    url = 'https://pro-api.coinmarketcap.com/v1/global-metrics/quotes/latest?convert='+country
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'API_KEY',
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url)
        results = response.json()
        print("For "+country+":\n")
        print(response)
        print(json.dumps(results, sort_keys=True, indent=4))

        active_currency = results["data"]["active_cryptocurrencies"]
        active_markets = results["data"]["active_market_pairs"]
        bitcoin_percentage = results["data"]["btc_dominance"]
        last_updates = results["data"]["last_updated"]
        global_cap = int(results["data"]["quote"][country]["total_market_cap"])
        global_volume = int(results["data"]["quote"][country]["total_volume_24h"])

        active_currency_str = '{:,}'.format(active_currency)
        active_markets_str = '{:,}'.format(active_markets)
        global_cap_str = '{:,}'.format(global_cap)
        global_volume_str = '{:,}'.format(global_volume)

        x = datetime.timestamp(datetime.strptime(last_updates, "%Y-%m-%dT%H:%M:%S.%fZ"))
        last_updates_date = datetime.fromtimestamp(x).strftime('%B %d,%Y at %I:%M%p')

        print("Active Currency :", active_currency)
        print("Active Market :", active_markets)
        print("Bitcoin Percentage :", str(bitcoin_percentage) + "%")
        print("Last Updated :", last_updates)
        print("Global Capital :", global_cap)
        print("Global volume :", global_volume)

        print("======================================")
        print("There are currently " + active_currency_str + " active cryptocurrencies and " + active_markets_str + ".")
        print("The global cap of all crypto is " + global_cap_str + " and the 24th global volume is :" + global_volume_str)
        print("Bitcoin\'s total percentage of the global cap is " + str(bitcoin_percentage) + "%\n")

        print("The Information was last updated on :", last_updates_date)
        print("======================================")
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
