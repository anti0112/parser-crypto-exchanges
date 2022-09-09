import aiohttp
import asyncio
import json
from tools.utils import get_url_spot

with open('spot.json', 'w') as f:
    f.write("[")


urls = get_url_spot() 
   
async def call_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            resp = await response.json()
            with open("spot.json", "a") as f:
                json.dump(resp, f)
                f.write(',')
                  
                                 
futures = [call_url(url) for url in urls]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(futures))
            
with open('spot.json', 'a') as f:
    f.write("]")     