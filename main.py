from typing import Optional

from fastapi import FastAPI,Header,Request

app = FastAPI()
ips = {}

@app.get("/")
def read_root():
    return ips

@app.get("/flush/{server_name}")
def read_ip(server_name: str, request: Request):
    client_host = request.client.host
    if server_name in ips:
        ips[server_name] = client_host
    else:
        ips[server_name] = client_host
    return ips

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}