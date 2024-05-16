from typing import Annotated
from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates

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


@router.get("/user")
def list_users(
    request: Request,
    user_repo: Annotated[db.UserRepository, Depends(db.UserRepository)],
):
    users = user_repo.get_all()
    return templates.TemplateResponse(
        "list_users",
        context={
            "request": request,
            "users": users,
        },
    )
