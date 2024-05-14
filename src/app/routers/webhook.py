from fastapi import APIRouter, Depends, Response, status
from typing import Annotated
import db

from ..schemas import SMS


router = APIRouter(
    prefix="/webhook",
    tags=["webhook"],
)


@router.post("/")
async def webhook(
    sms: SMS,
    user_repo: Annotated[db.UserRepository, Depends(db.UserRepository)],
    reached_repo: Annotated[db.ReachedRepository, Depends(db.ReachedRepository)],
    resp: Response,
):
    user = user_repo.get_by_phone(sms.phone)
    if user:
        reached = reached_repo.insert(user.id)
        return {
            "message": "Hello, World!",
            "msisdn": sms.phone,
            "text": sms.text,
            "message_ID": sms.messageId,
            "reached_id": reached.id,
        }
    else:
        resp.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        return {
            "message": "User not found",
            "msisdn": sms.phone,
        }
