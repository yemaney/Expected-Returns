import uvicorn
from fastapi import FastAPI

try:
    from scraper import cape_ratio
except ImportError:
    from .scraper import cape_ratio

app = FastAPI()


@app.get("/")
async def read_root():
    return "Expected Returns FastAPI Backend Root Landing Page"


@app.post("/expected-returns/{scope}")
async def read_cape(scope: str):
    result = cape_ratio(scope)
    return result


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
