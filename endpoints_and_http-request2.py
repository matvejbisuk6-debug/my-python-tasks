from typing import Annotated

from fastapi import FastAPI, Query
from pydantic import BaseModel, Field, EmailStr, model_validator

app = FastAPI()

#Задача 1
class Check(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=24)
    age: int = Field(min_length=18, max_length=100)

@app.post("/auth/register")
def registration(win_reg: Check):
    return win_reg.model_dump()

#Задача 2
class Python(BaseModel):
    parameters1: Annotated[str,
        Field(default=None, min_length=5)
    ]
    parameters2: Annotated[str,
        Field(default=None, min_length=3)
    ]

@app.get("/items")
def get_parameters(parameters: Annotated[Python, Query()]):
    return {"per_page": parameters.parameters1, "page_number": parameters.parameters2}

#Задача 3
class Check(BaseModel):
    check_in: str
    check_out: str

@model_validator(mode="after")
def check_bookings(self) -> "Check":
    if self.check_in != self.check_out:
        raise ValueError("Ошибка")
    return self

@app.post("/bookings")
def hotel_booking(check_booking: Check):
    return {"check_in": check_booking.check_in, "check_out": check_booking.check_out}

#Задача 4
