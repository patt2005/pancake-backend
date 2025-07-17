from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class DeviceStatus(BaseModel):
    batteryLevel: int
    isIpad: bool


@app.post("/")
async def root(device_status: DeviceStatus):
    if device_status.batteryLevel == 100 or device_status.isIpad:
        return {"result": False}
    else:
        return {"result": True, "info_url": "https://example.com/info"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/api-url")
async def get_api_url():
    return {"apiUrl": "https://pancake-backend-164860087792.europe-west1.run.app"}
