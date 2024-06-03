from functools import lru_cache
from fastapi import FastAPI, HTTPException

app = FastAPI()


@lru_cache(maxsize=20)
def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("El número debe ser un entero no negativo.")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


@app.get("/get_fibonacci/{n}", response_model=int)
def get_fibonacci(n: int):
    try:
        result = fibonacci(n)
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


if __name__ == "__main__":  # pragma: no cover
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
