from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, List, Optional

app = FastAPI(
    title="API de Exemplo - FastAPI",
    description="Starter code para a assignment 'Construindo APIs REST com FastAPI'",
)


class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None


# In-memory "DB"
db: Dict[int, Item] = {}


@app.get("/", tags=["root"])
def read_root():
    return {"message": "FastAPI starter running"}


@app.get("/items", response_model=List[Item], tags=["items"])
def list_items():
    return list(db.values())


@app.post("/items", response_model=Item, tags=["items"])
def create_item(item: Item):
    if item.id in db:
        raise HTTPException(status_code=400, detail="Item with this id already exists")
    db[item.id] = item
    return item


@app.get("/items/{item_id}", response_model=Item, tags=["items"])
def get_item(item_id: int):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item not found")
    return db[item_id]


@app.put("/items/{item_id}", response_model=Item, tags=["items"])
def update_item(item_id: int, item: Item):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item not found")
    db[item_id] = item
    return item


@app.delete("/items/{item_id}", tags=["items"])
def delete_item(item_id: int):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item not found")
    del db[item_id]
    return {"ok": True}


# Nota: Para executar localmente:
# 1) Instale dependências: pip install fastapi uvicorn
# 2) Rode: uvicorn starter-code:app --reload --port 8000
# 3) Abra: http://localhost:8000/docs
