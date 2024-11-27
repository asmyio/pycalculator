from fastapi import FastAPI, HTTPException

app = FastAPI()

# Simple calculation function
def calculation(num1: int, num2: int, operation: str) -> int:
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    else:
        raise ValueError("Invalid operation. Only '+' or '-' are supported.")

# POST request to handle calculation with JSON body (no class)
@app.post("/calculate/")
async def calculate_post(first_number: int, second_number: int, operation: str):
    try:
        result = calculation(first_number, second_number, operation)
        return {"result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# GET request to handle calculation with query parameters (no class)
@app.get("/calculate/")
async def calculate_get(first_number: int, second_number: int, operation: str):
    try:
        result = calculation(first_number, second_number, operation)
        return {"result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
