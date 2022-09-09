import requests
url = 'https://www.okx.com/priapi/v5/market/trades'
params = {"t":1658398229222,
        "instId":"BTC-USDT"}

resp = requests.get(url, params=params)
print(resp.text)

