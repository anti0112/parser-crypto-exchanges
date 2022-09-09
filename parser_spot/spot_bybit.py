import requests

params = {"symbol": f"301.BTCUSDT", "interval": "1m", "limit": 10, "r": 1658397760920}
spot = "https://api2.bybit.com/spot/api/quote/v2/klines"
response = requests.get(spot, params=params)
print(response.text)