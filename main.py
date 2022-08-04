from typing import Union
import uvicorn
import os
from fastapi import FastAPI
from utils import PrometheusMiddleware, metrics, setting_otlp


# port = os.environ["PORT"]
port = 8000
APP_NAME = 'fastapi_cicd_testing'
app = FastAPI()
app.add_middleware(PrometheusMiddleware, app_name=APP_NAME)
app.add_route("/metrics", metrics)


@app.get("/")
def read_root():
    return {"data": "Application ran successfully - FastAPI release v2.0"}


@app.get("/items/{item_id}")
def read_item(item_id: int, qq: str = None):
    return {"item_id": item_id, "qq": qq}


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=port, reload=False)  
