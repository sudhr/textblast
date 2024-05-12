from typing import Annotated
from fastapi import APIRouter, Depends, FastAPI, Response, status
from pydantic.types import Strict
from sqlalchemy.orm import Session

from .routers import webhook

import db
from .schemas import SMS

app = FastAPI()
StrictMSISDN = Annotated[str, Strict()]

app.include_router(webhook.router)
