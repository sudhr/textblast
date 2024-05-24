from typing import Annotated

from fastapi import APIRouter, Depends, Response, status
from tb_storage import UserRepository

from ..schemas.sms import SMS

router = APIRouter(
    prefix="/api",
    tags=["api"],
)


@router.post("/webhook")
async def webhook(
    sms: SMS,
    user_repo: Annotated[UserRepository, Depends(UserRepository)],
    resp: Response,
):
    user = user_repo.get_by_phone(sms.phone)
    if user:
        # reached = reached_repo.insert(user.id)
        return {
            "message": "Hello, World!",
            "msisdn": sms.phone,
            "text": sms.text,
            "message_ID": sms.messageId,
        }
    else:
        resp.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        return {
            "message": "User not found",
            "msisdn": sms.phone,
        }
