# tools.py
import requests

def get_price(symbol="BTCUSDT") -> str:
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol.upper()}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return f"💰 The current price of {symbol.upper()} is ${float(data['price']):,.2f}"
    else:
        return "⚠️ Failed to fetch the price. Maybe the symbol is incorrect?"
