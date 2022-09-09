import asyncio
import aiohttp
import json
from tools.utils import get_url_for_bybit


pay = ['BUY', 'SELL']
url = "https://api2.bybit.com/spot/api/otc/item/list"

list_buy, list_sell = get_url_for_bybit()

for i in pay:
    with open(f'bybit_{i}.json', "w") as f:
        f.write('[')
        
        
id = 0
for buy_sell_list in [list_buy, list_sell]:
    async def call_url(data):
        async with aiohttp.ClientSession() as session:
            async with session.post(url, data=data) as response:
                resp = await response.json()
                with open(f"bybit_{pay[id]}.json", "a") as f:
                    json.dump(resp, f)
                    f.write(',')
                  
                                 
    futures = [call_url(data) for data in buy_sell_list]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(futures))
    id += 1

for i in pay:
    with open(f'bybit_{i}.json', "a") as f:
        f.write(']')
    
