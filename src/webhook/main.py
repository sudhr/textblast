from typing import Annotated
from fastapi import FastAPI
from pydantic import BaseModel, Field
from pydantic.types import Strict

app = FastAPI()

StrictMSISDN = Annotated[str, Strict()]


class SMSPostBody(BaseModel):
    msisdn: str = Field(min_length=11, max_length=11, pattern="^\\d{11}$")
    text: str = Field(min_length=1)


@app.post("/webhook")
async def webhook(sms: SMSPostBody):
    return {"message": "Hello, World!", "msisdn": sms.msisdn, "text": sms.text}
