import asyncio
import re

async def handle_client(reader, writer):
    request = await reader.read(1024)
    request_str = request.decode()
    
    # Parse request to get pesel from URL
    # Extract from: GET /users/{pesel} HTTP/1.1
    match = re.search(r'/users/(\d+)', request_str)
    pesel = match.group(1) if match else None
    
    if not pesel:
        writer.write(b"HTTP/1.1 400 Bad Request\r\n\r\n")
        writer.close()
        return
    
    # Make HTTP GET to FastAPI
    reader2, writer2 = await asyncio.open_connection('127.0.0.1', 8000)
    get_request = f"GET /users/{pesel} HTTP/1.1\r\nHost: 127.0.0.1:8000\r\n\r\n"
    writer2.write(get_request.encode())
    await writer2.drain()
    
    response = await reader2.read(1024)
    writer.write(response)
    await writer.drain()
    writer.close()

async def main():
    server = await asyncio.start_server(handle_client, '127.0.0.1', 8001)
    await server.serve_forever()

asyncio.run(main())