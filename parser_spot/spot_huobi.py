
import requests

url = 'https://www.huobi.com/en-us/exchange/'

respose = requests.get(url)

print(respose.text)