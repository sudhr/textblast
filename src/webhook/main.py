from typing import Annotated
from fastapi import FastAPI
from pydantic import BaseModel, Field
from pydantic.types import Strict

app = FastAPI()

StrictMSISDN = Annotated[str, Strict()]


class SMS(BaseModel):
    msisdn: str = Field(
        alias="msisdn", min_length=11, max_length=11, pattern="^\\d{11}$"
    )
    text: str = Field(alias="text", min_length=1)
    messageId: str = Field(alias="messageID", min_length=5, max_length=64)


@app.post("/webhook")
async def webhook(sms: SMS):
    return {
        "message": "Hello, World!",
        "msisdn": sms.msisdn,
        "text": sms.text,
        "message_ID": sms.messageId,
    }
