import requests
url = "https://bitzlato.bz/api/v2/peatio/public/markets/eth_btc/trades"

resp = requests.get(url)
print(resp.text)
