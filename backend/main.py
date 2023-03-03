from typing import Union

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware
import schemas, models
import crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = {
    "http://localhost",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://127.0.0.1"
}

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"Hello" : "World"}

# @app.get("/items/{item_id}")
# # A "path" is also commonly called an "endpoint" or a "route".
# # "path" is the main way to separate "concerns" and "resources".
# def read_item(item_id: int, q: Union[str, None] = None):
#     #Union 여러개의 타입 허ㅇ
#     return {"item_id": item_id, "q": q}
@app.get("/board/{idx}")
async def get_board(idx: int, db: Session = Depends(get_db)):
    return crud.get_board(db, idx)

@app.get("/board/list/{page}")
async def get_board(page: int = 1, limit: int = 10, db: Session = Depends(get_db)):
    offset = (page-1)*limit
    return crud.get_boards(db, offset, limit)

@app.post("/board/")
async def create_board(board: schemas.BoardCreate, db: Session = Depends(get_db)):
    
    board = crud.create_board(db, board)
    return board

@app.delete("/board/{idx}")
async def delete_board(idx: int, db: Session = Depends(get_db)):
    return crud.delete_board(db, idx)

