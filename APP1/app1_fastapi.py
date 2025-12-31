import aiohttp
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/{pesel}')
async def root(pesel: int):
    async with aiohttp.ClientSession() as session:
        # async with session.get(f'http://127.0.0.1:8000/users/{pesel}') as resp:
        #     return await resp.json()
        print('We are inside App1 Fastapi')
        response = await session.get(f'http://127.0.0.1:8000/users/{pesel}')
        return response.json()
    
@app.get('/')
def hello():
    return 'app1 fastapi is alive!'    
    
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)