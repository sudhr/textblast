from typing import Annotated
from fastapi import APIRouter, Depends, FastAPI
from pydantic import BaseModel, Field
from pydantic.types import Strict
from sqlalchemy.orm import Session


from db.database import SessionLocal, engine
from db import crud, models, schemas

app = FastAPI()
router = APIRouter()

StrictMSISDN = Annotated[str, Strict()]

models.Base.metadata.create_all(bind=engine)


# Depenendency injection
def get_db_session():
    sl = SessionLocal()
    try:
        yield sl
    finally:
        sl.close()


class SMS(BaseModel):
    msisdn: str = Field(
        alias="msisdn", min_length=11, max_length=11, pattern="^\\d{11}$"
    )
    text: str = Field(alias="text", min_length=1, max_length=250)
    messageId: str = Field(alias="messageID", min_length=5, max_length=64)


@router.post("/webhook")
async def webhook(sms: SMS, session: Session = Depends(get_db_session)):
    user: models.User = crud.get_user(session, sms.msisdn)
    crud.create_reached(
        session, schemas.ReachedCreate(user.id, timestamp=sms.timestamp)
    )
    return {
        "message": "Hello, World!",
        "msisdn": sms.msisdn,
        "text": sms.text,
        "message_ID": sms.messageId,
    }
