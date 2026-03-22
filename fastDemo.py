from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel

app = FastAPI()


some_items = []

class Item(BaseModel):
	name: str


@app.get("/")
def read_root():
	return {"items": len(some_items)}


@app.get("/items/{item_id}")
def read_item(item_id: int) -> Item:
	if item_id >= len(some_items):
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='det item_id er for højt')
	return some_items[item_id]


@app.post("/items/")
def create_item(item: Item):
	some_items.append(item)
	return {"items": len(some_items)}

