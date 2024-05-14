from typing import Annotated
from fastapi import FastAPI
from pydantic.types import Strict

from .routers import webapp, webhook


app = FastAPI()
StrictMSISDN = Annotated[str, Strict()]

# Register Routers
app.include_router(webhook.router)
app.include_router(webapp.router)
