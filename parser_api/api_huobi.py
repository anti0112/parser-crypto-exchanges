import aiohttp
import asyncio
import json
from tools.utils import get_url_for_huobi

pay = ['BUY', 'SELL']
for i in pay:
    with open(f'huobi_{i}.json', 'w') as f:
        f.write("[")


list_buy, list_sell = get_url_for_huobi() 
id = 0
for buy_sell_list in [list_buy, list_sell]:
    async def call_url(url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                resp = await response.json()
                with open(f"huobi_{pay[id]}.json", "a") as f:
                    json.dump(resp, f)
                    f.write(',')
                    
                                    
    futures = [call_url(url) for url in buy_sell_list]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(futures))
    id += 1
            
for i in pay:
    with open(f'huobi_{i}.json', 'a') as f:
        f.write("]")     