import asyncio
import aiohttp
import json
from utils import get_url_for_okx
from const import headers_okx

pay =['BUY', 'SELL']
list_buy, list_sell = get_url_for_okx()

for i in pay:
    with open(f"okx_{i}.json", 'w') as f:
        f.write("[")
 
id = 0
for buy_sell_list in [list_buy, list_sell]:   
    async def call_url(url):
        print(f"starting{url}")
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers_okx) as response:
                resp = await response.json()
                with open(f"okx_{pay[id]}.json", "a") as f:
                        json.dump(resp, f)
                        f.write(",")


    futures = [call_url(url) for url in buy_sell_list]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(futures))
    id += 1


for i in pay:
    with open(f"okx_{i}.json", 'a') as f:
        f.write("]")

