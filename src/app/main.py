from typing import Annotated
from fastapi import FastAPI
from pydantic.types import Strict

from .routers import api, webapp


app = FastAPI()
StrictMSISDN = Annotated[str, Strict()]

# Register Routers
# webapp.router.include_router(api.router)
app.include_router(api.router)
app.include_router(webapp.router)
