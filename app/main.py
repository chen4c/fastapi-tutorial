from fastapi import FastAPI
from .routers import users

app = FastAPI()
app.include_router(users.router)


@app.get("/")
async def get_home():
    return {"main": "Hello, World!"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="localhost", port=8000, reload=True)
