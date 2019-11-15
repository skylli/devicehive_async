import aiohttp,logging
import asyncio

argc = {"json":{"login": "sky", "password": "sky9527"}, "params":{},"headers":{}}
async def main(session):
    async with session.request("POST",'http://192.168.0.12/api/rest/token', **argc) as response:
        print("Status:", response.status)
        print("Content-type:", response.headers['content-type'])

        html = await response.text()
        print("Body:", html, "...")
    await session.close()

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
loop = asyncio.get_event_loop()
session = aiohttp.ClientSession()
loop.run_until_complete(main(session))


