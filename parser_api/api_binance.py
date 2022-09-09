import asyncio
import aiohttp
import json
from tools.utils import get_list_of_data
import time

url = 'https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search'
pay = ['BUY', 'SELL']

# Очищение файлов json от старых записей
for i in pay:
    with open(f'binance_{i}.json', "w") as f:
        f.write('[')

list_sell, list_buy = get_list_of_data()

k = 0

strt = time.time()
for buy_sell_list in [list_buy, list_sell]:
    async def call_url(data):
        print(f'Starting {data["page"]}')
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=data) as response:
                resp = await response.json()
                if not resp['code'] == '000002':
                    with open(f"binance_{pay[k]}.json", "a") as f:
                        json.dump(resp, f)
                        f.write(',')
                  
                                 
    futures = [call_url(data) for data in buy_sell_list]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(futures))
    k += 1
    
for i in pay:
    with open(f'binance_{i}.json', "a") as f:
        f.write(']')
        
end = time.time()
print(end - strt)
