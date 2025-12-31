from aiohttp import web
import aiohttp
import asyncio

async def fetch_user(pesel):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'http://127.0.0.1:8000/users/{pesel}') as resp:
            return await resp.json()

async def proxy_handler(request):
    pesel = request.match_info['pesel']
    data = await fetch_user(pesel)
    return web.json_response(data)

async def main():
    app = web.Application()
    app.router.add_get('/users/{pesel}', proxy_handler)
    
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '127.0.0.1', 8001)
    await site.start()
    
    print('Server started on http://127.0.0.1:8001')
    await asyncio.Event().wait()

if __name__ == '__main__':
    asyncio.run(main())