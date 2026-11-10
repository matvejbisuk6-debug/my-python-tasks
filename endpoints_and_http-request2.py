import hashlib
from typing import Annotated

from fastapi import FastAPI, Query
from pydantic import BaseModel, Field, EmailStr, model_validator, ConfigDict

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
class OrderItem(BaseModel):
    product_id: int
    quantity: int = Field(ge=1)

class OrderCreate(BaseModel):
    customer_id: int
    items: list[OrderItem]

@app.post("/orders")
def total_quantity(total: OrderCreate):
    total_qty = sum(item.quantity for item in total.items)
    return {"items": total, "total_amount": total_qty}

#Задача 5
#На выход
class EmployeeCreate(BaseModel):
    name: str
    email: EmailStr
    password: int
    salary: int

class EmployeeResponse(BaseModel):
    id: str
    name: str
    email: EmailStr
    password: str
    salary: int

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode("utf-8")).hexdigest()

def hash_salary(salary: int) -> str:
    return hashlib.sha256(str(salary).encode()).hexdigest()

@app.get("/employees/{id}", response_model=EmployeeCreate)
def viewing(int: int):
    return {
        "id": id,
        "name": "Matvey",
        "email": "matvey@example.com"
    }

@app.post("/employees", response_model=EmployeeResponse)
def get_employee(Response: EmployeeResponse):
    hashed_password = hash_password(Response.password)

    hashed_salary = hash_salary(Response.salary)

    print(f"Сохраняем в базу пароль: {hash_password}")

    print(f"Сохраняем в базу зарплату: {hash_salary}")

    db_employee_data = {
        id: 1,
        "name": Response.name,
        "email": Response.email,
        "password": hashed_password,
        "salary": hashed_salary
    }

    return db_employee_data

#Задача 6
class DBUser:
    def __init__(self, id: int, username: str, hashed_password: str):
        self.id = id
        self.username = username
        self.hashed_password = hashed_password

class User(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    username: str

@app.get("/users/me",response_model=User)
def get_json():
    db = DBUser(id=1, username="Матвей", hashed_password="sdgyasydgwm")
    return db