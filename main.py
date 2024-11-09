from fastapi import FastAPI

app = FastAPI(title="Calculator")


@app.get("/multiply")
def multiply(a: float, b: float) -> float:
    return a * b


@app.get("/add")
def add(a: float, b: float) -> float:
    return a + b


@app.get("/subtract")
def subtract(a: float, b: float) -> float:
    return a - b


@app.get("/divide")
def divide(a: float, b: float) -> float:
    return a / b
