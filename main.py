from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/api-url")
async def get_api_url():
    return {"apiUrl": "https://pancake-backend-164860087792.europe-west1.run.app"}
