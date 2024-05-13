from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="src/app/templates")


@router.get("/")
def index(request: Request):
    return templates.TemplateResponse("home.html", context={"request": request})


@router.get("/conversation")
def conversation(request: Request):
    return templates.TemplateResponse("conversation.html", context={"request": request})
