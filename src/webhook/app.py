from typing import Annotated
from fastapi import APIRouter, Depends, FastAPI, Response, status
from pydantic.types import Strict
from sqlalchemy.orm import Session

import db
from .schemas import SMS

app = FastAPI()
router = APIRouter()

StrictMSISDN = Annotated[str, Strict()]


@router.post("/webhook")
async def webhook(
    sms: SMS,
    user_repo: Annotated[db.UserRepository, Depends(db.UserRepository)],
    reached_repo: Annotated[db.ReachedRepository, Depends(db.ReachedRepository)],
    resp: Response,
):
    user = user_repo.get_by_phone(sms.msisdn)
    if user:
        reached = reached_repo.insert(user.id)
        return {
            "message": "Hello, World!",
            "msisdn": sms.msisdn,
            "text": sms.text,
            "message_ID": sms.messageId,
        }
    else:
        resp.status_code = status.HTTP_400_BAD_REQUEST
        return {
            "message": "User not found",
            "msisdn": sms.msisdn,
        }


app.include_router(router)
