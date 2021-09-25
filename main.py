from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import datetime


class Coffee(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
    star: int


coffeeDb = [
    {
        "id": 1,
        "name": "Coffee A",
        "description": "เช้มข้นจัด",
        "price": 490.0,
        "star": 4
    },
    {
        "id": 2,
        "name": "Coffee B",
        "description": "เช้มข้น",
        "price": 400.0,
        "star": 3
    }
]

app = FastAPI()


@app.get("/")
async def root():
    return {
        "date": datetime.datetime.now(),
        "msg": "hello"
    }


@app.get("/coffees")
async def gatCoffees():
    return coffeeDb


@app.get("/coffees/{id}")
async def getCoffee(id: int):
    for val in coffeeDb:
        if val["id"] == id:
            return val
    return "not found"


@app.post("/coffees")
async def createCoffee(body: Coffee):
    coffeeDb.append(body)
    return coffeeDb[-1]


@app.delete("/coffees")
async def deleteCoffee(id: int):
    index = -1
    for i, val in enumerate(coffeeDb):
        if val["id"] == id:
            index = i
            break
    if index == -1:
        return "not found"

    del coffeeDb[index]
    return coffeeDb
