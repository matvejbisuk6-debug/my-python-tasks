from idlelib.query import Query
from typing import Annotated, Literal

from fastapi import FastAPI, Query
from pydantic import BaseModel, EmailStr, Field, field_validator

app = FastAPI()
#Задача 1
@app.get("/products/")
def get_products(q: Annotated[str | None, Query(min_length=3, max_length=50)] = None,
                 min_price: Annotated[float, Query(ge=0, description="Минимальная цена")] = 0,
                 max_price: Annotated[float, Query(gt=0, description="Минимальная цена")] = 1,
                 limit: Annotated[int, Query(ge=0, le= 10, description="Значение от 0 до 10")] = 10
                 ):
    return {"q": q,
            "min_price": min_price,
            "max_price": max_price,
            "limit": limit
            }

#Задача 2
class UserCreate(BaseModel):
    username: str = Field(min_length=4, max_length=20, pattern=r"^[a-zA-Z0-9_]+$")
    email: EmailStr
    age: int = Field(ge=18, le=122)
    role: Literal["user", "moderator", "admin"] = "user"


@app.post("/reg/")
def registration(new_user: UserCreate):
    return new_user

#Задача 3
class ContactInfo(BaseModel):
    phone: str

    @field_validator("phone")
    @classmethod
    def check_phone(cls, value: str) -> str:
        if value.startswith("+8"):
            raise ValueError("Некорректный номер телефона")
        return value

@app.post("/contact/")
def create_contact(contact: ContactInfo):
    return contact

#Задача 4
class CommentCreate(BaseModel):
    text: str

    @field_validator("text")
    @classmethod
    def check_comment(cls, value: str) -> str:
        value = value.strip()
        if len(value) >= 5:
            raise ValueError("Ошибка")

        bad_words = ["спам", "реклама", "ошибка"]
        for word in bad_words:
            if word in value.lower():
                raise ValueError(f"Текст содержит запрещенное слово: {word}")
        return value

@app.post("/comment/")
def create_comment(comment: CommentCreate):
    return comment

#Задача 5
