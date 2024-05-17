from typing import Annotated
from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from starlette import status

from app.schemas import UserForm
import db

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


@router.post("/user/add")
def add_user_form_post(
    request: Request,
    user_repo: Annotated[db.UserRepository, Depends(db.UserRepository)],
    uf: UserForm = Depends(UserForm),
):
    dbUser = db.User(fname=uf.fname, lname=uf.lname, phone=uf.phone)
    user_repo.insert(dbUser)
    return RedirectResponse(url="/user", status_code=status.HTTP_302_FOUND)


@router.get("/user")
def list_users(
    user_repo: Annotated[db.UserRepository, Depends(db.UserRepository)],
    request: Request,
):
    users = user_repo.get_all()
    return templates.TemplateResponse(
        "list_users",
        context={
            "request": request,
            "users": users,
        },
    )
