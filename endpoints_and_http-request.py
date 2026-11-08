from typing import Annotated
from fastapi import HTTPException, Path, FastAPI
from pydantic import BaseModel, Field

#Задача 1 get - запросы
app = FastAPI()

@app.get("/search")
def get_json(query: str | None, page: int):
    if query is None:
        raise HTTPException(
            status_code=404,
            detail=f"Query '{query}' not found"
        )
    return {"query": query, "page": page}

#Задача 2
@app.get("/users/{user_id}")
def get_path_json(user_id: Annotated[int, Path(title="ID получаемого товара", ge=1,le=1000)], status: str):
    return {"user_id": user_id, "status": status}

#Задача 3
class UserCreate(BaseModel):
    name: str = Field(min_length=3,max_length=50),
    price: float = Field(gt=0),
    in_stock: bool = True

@app.post("/products")
def create_resources(name: UserCreate):
    if len(name.name) > 50:
        raise HTTPException(
            status_code=400,
            detail="Слишком длинное имя"
        )
    return {"status": "success", "data": name.model_dump()}

#Задача 4
@app.put("/products/{product_id}", status_code=202)
def updatate_product(product_id: int, payload: UserCreate):
    if product_id > 1000:
        raise HTTPException(
            status_code=404,
            detail="Товар не найден"
        )
    return {
        "status": "updated",
        "product_id": product_id,
        "updated_data": payload.model_dump()
    }