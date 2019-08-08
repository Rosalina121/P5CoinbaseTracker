from coinbase.wallet.client import Client

api_key = "your api key here"
api_secret = "your secret here"

client = Client(api_key, api_secret)

currencies = client.get_currencies()

ETHAccount = client.get_account("eth acc id")
BTCAccount = client.get_account("btc acc id")

BTC = client.get_buy_price(currency_pair="BTC-USD")["amount"]
ETH = client.get_buy_price(currency_pair="ETH-USD")["amount"]

currentBTC = BTCAccount["balance"]["amount"]
currentETH = ETHAccount["balance"]["amount"]

BTCUSD = BTCAccount["native_balance"]["amount"]
ETHUSD = ETHAccount["native_balance"]["amount"]

balance = str(round(float(BTCUSD) + float(ETHUSD), 2))

f = open(r'C:\Users\<you>\Documents\Rainmeter\Skins\LuaTextFile\Test.txt', 'w')
# Prepare for the worst...
f.write("Current balance: $" + balance + "\n\nBitcoin: " + currentBTC + " = $" + BTCUSD + "\nEthereum: " + currentETH + " = $" + ETHUSD + "\n\nBTC: $" + BTC + "\nETH: $" + ETH)
f.close()
