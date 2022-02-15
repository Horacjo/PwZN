import asyncio
import uuid
import aiohttp
import aiofiles
import async_timeout

async def get_url(url, session):    
    file_name = str(uuid.uuid4())
    async with async_timeout.timeout(120):
        async with session.get(url) as response:
            f = await aiofiles.open(file_name+'.png', mode='wb')
            await f.write(await response.read())
            await f.close()
    return 'Successfully downloaded ' + file_name

async def main(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [get_url(url, session) for url in urls]
        return await asyncio.gather(*tasks)

urls = ["https://www.learningcontainer.com/wp-content/uploads/2020/08/Sample-Image-file-Download.png",
        "https://www.learningcontainer.com/wp-content/uploads/2020/08/Sample-Small-Image-PNG-file-Download.png",
        "https://www.learningcontainer.com/wp-content/uploads/2020/08/Sample-Small-Image-PNG-file-Download.png"]

loop = asyncio.get_event_loop()
results = loop.run_until_complete(main(urls))

print('\n'.join(results))