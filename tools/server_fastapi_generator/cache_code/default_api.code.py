from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from server_fastapi.auto_gen.database import get_db

default_api = APIRouter()

@default_api.get("/")
async def read_user_me(db: Session = Depends(get_db)):
    # db: Session = get_db()
    rs = db.execute(
        "SELECT * FROM account;"
    ).all()
    
    return rs