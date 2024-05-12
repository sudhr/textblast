from typing import Annotated
from fastapi import APIRouter, Depends, FastAPI, Response, status
from pydantic.types import Strict
from sqlalchemy.orm import Session

from .routers import webhook, index

import db
from .schemas import SMS

app = FastAPI()
StrictMSISDN = Annotated[str, Strict()]

# Register Routers
app.include_router(webhook.router)
app.include_router(index.router)
