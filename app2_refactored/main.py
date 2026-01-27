from fastapi import FastAPI
import uvicorn
from models import create_db_tables, create_dummy_users
from routes import router

app = FastAPI()

app.include_router(router, prefix="/users")

@app.on_event("startup")
async def on_startup():
    create_db_tables()
    create_dummy_users()

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8002)