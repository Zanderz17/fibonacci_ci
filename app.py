from fastapi import FastAPI

app = FastAPI()

if __name__ == "__main__":  # pragma: no cover
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
