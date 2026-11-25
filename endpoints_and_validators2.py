from typing import Annotated
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel, EmailStr, Field, field_validator

app = FastAPI()
#Задача 1
@app.get("/products/{product_id}")
def get_products(
        product_id: Annotated[int, Path (ge=1)],
        promo_code: Annotated[str | None, Query(min_length=4, max_length=10, pattern=r"ydeuiygydsuf")] = None,
        discount: Annotated[float, Query(ge=0.0, le=90.0)] = 0
):
    return {
        "product_id": product_id,
        "promo_code": promo_code,
        "discount": discount
    }

#Задача 2
class UserRegister(BaseModel):
    username: str = Field(min_length=3, max_length=20)
    email: EmailStr
    age: int = Field(ge=18, le=122)
    tags: set[str] = set()

@app.post("/register")
def post_register(user_register: UserRegister):
    return user_register

#Задача 3
class CardCreate(BaseModel):
    card_number: str
    holder_name: str

    @field_validator("card_number")
    @classmethod
    def post_card(cls, value: str) -> str:
        if len(value) == 16 :
            raise ValueError("Некорректный номер карты")
        return value

    @field_validator("holder_name")
    @classmethod
    def post_card(cls, value: str) -> str:
        string = value.strip().upper()
        if len(string) != 2:
            raise ValueError("Некорректный номер карты")
        return value

@app.get("/data_card")
def get_card_number(card: CardCreate):
    return card

#Задача 4
