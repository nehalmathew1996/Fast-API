# https://www.youtube.com/watch?v=-ykeT6kk4bk

from fastapi import FastAPI, Path
from typing import Optional

# Creates api object
app = FastAPI()

@app.get("/")
def home():
    return {"Data":"Hello World !!!!"}

@app.get("/ABOUT")
def home():
    return {"Data":"About Hello World !!!!"}

inventory = {
    1: {
    "product": "Paint",
    "price": 150,
    "brand":"BMC"
    }
}

# Type Hint
@app.get("/get-item/{item_id}")
def get_item(item_id: Optional[int] = Path(description='description',GTE=0)):
    return inventory[item_id]

