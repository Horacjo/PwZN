import asyncio
import uuid
import aiohttp
import async_timeout

async def get_url(url, session):    
    file_name = str(uuid.uuid4())
    async with async_timeout.timeout(120):
        async with session.get(url) as response:
            with open(file_name, 'wb') as fd:
                async for data in response.content.iter_chunked(1024):
                    fd.write(data)
    return 'Successfully downloaded ' + file_name

async def main(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [get_url(url, session) for url in urls]
        return await asyncio.gather(*tasks)

urls = ["https://github.com/brokenpumpernickel/PwZN-2021Z-Live/blob/master/lab/lab010/async02.py",
        "https://github.com/brokenpumpernickel/PwZN-2021Z-Live/blob/master/lab/lab010/async01.py",
        "https://github.com/brokenpumpernickel/PwZN-2021Z-Live/blob/master/lab/lab010/coroclient.py",
        "https://github.com/brokenpumpernickel/PwZN-2021Z-Live/blob/master/lab/lab010/coroserver.py"]

loop = asyncio.get_event_loop()
results = loop.run_until_complete(main(urls))

print('\n'.join(results))