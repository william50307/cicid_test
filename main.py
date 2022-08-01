from typing import Union
import uvicorn
import os
from fastapi import FastAPI

# port = os.environ["PORT"]
port = '8000'

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, qq: str = None):
    return {"item_id": item_id, "qq": qq}


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=port, reload=False)  
