import uvicorn
from fastapi import Depends, FastAPI
from sqlmodel import Session, select

try:
    from database import create_db_and_tables, engine
    from models import CountryCape, GlobalCape
except ImportError:
    from .database import create_db_and_tables, engine
    from .models import CountryCape, GlobalCape

app = FastAPI()


def reshape(data: dict) -> dict:
    new = {}
    for k, v in data.items():
        for i, j in v.items():
            try:
                new[i][k] = j
            except KeyError:
                new[i] = {}
                new[i][k] = j
    return new


def get_session():
    with Session(engine) as session:
        yield session


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


scopes = {"World": GlobalCape, "Country": CountryCape}


@app.post("/{scope}")
async def update_database(
    *, session: Session = Depends(get_session), capes: dict, scope: str
) -> dict:
    ret = reshape(capes)

    cape = scopes[scope]
    new = []
    if scope == "World":
        dates = session.exec(select(cape.date)).all()

        # for date in dates:
        for _, elem in ret.items():
            if elem["date"] not in dates:
                new.append((elem))

    elif scope == "Country":
        data = session.exec(select(cape.date, cape.country)).all()
        datas = []
        for elem in data:
            datas.append([elem["date"], elem["country"]])

        for _, elem in ret.items():
            x = [elem["date"], elem["country"]]
            if x not in datas:
                new.append(elem)

    if new:
        for data in new:
            gc = cape(**data)
            session.add(gc)
        session.commit()

    return {"Message": f"Completed update of {scope} table in database!"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
