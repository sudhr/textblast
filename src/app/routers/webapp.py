from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="src/app/templates")


@router.get("/")
def index(request: Request):
    return templates.TemplateResponse("home", context={"request": request})


@router.get("/conversation")
def conversation(request: Request):
    return templates.TemplateResponse("conversation", context={"request": request})


@router.get("/user/add")
def add_user_form(request: Request):
    return templates.TemplateResponse("add_user_form", context={"request": request})


@router.get("/user")
def list_users(request: Request):
    return templates.TemplateResponse("list_users", context={"request": request})
