from fastapi import FastAPI, HTTPException
from app.schemas import Item

app = FastAPI()

fake_db: list[dict] = []


@app.get("/")
def read_root():
    return {"status": "ok", "message": "Backend is running"}


# Create
@app.post("/items/")
def create_item(item: Item):
    fake_db.append(item.dict())
    return {"message": "Item created", "item": item}


# Read all
@app.get("/items/")
def list_items():
    return fake_db


# Read one
@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in fake_db:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")


# Update
@app.put("/items/{item_id}")
def update_item(item_id: int, updated_item: Item):
    for idx, item in enumerate(fake_db):
        if item["id"] == item_id:
            fake_db[idx] = updated_item.dict()
            return {"message": "Item updated", "item": updated_item}
    raise HTTPException(status_code=404, detail="Item not found")


# Delete
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for idx, item in enumerate(fake_db):
        if item["id"] == item_id:
            deleted_item = fake_db.pop(idx)
            return {"message": "Item deleted", "item": deleted_item}
    raise HTTPException(status_code=404, detail="Item not found")

