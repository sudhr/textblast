from typing import Annotated

from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from pydantic.types import Strict
from starlette import status

from .routers import api, webapp

app = FastAPI()
StrictMSISDN = Annotated[str, Strict()]
templates = Jinja2Templates(directory="src/app/templates")


# Exception handlers
@app.exception_handler(Exception)
async def exception_handler(request, exc):
    return templates.TemplateResponse(
        "error",
        context={
            "request": request,
            "exc": exc,
        },
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )


# Register Routers
# webapp.router.include_router(api.router)
app.include_router(api.router)
app.include_router(webapp.router)
