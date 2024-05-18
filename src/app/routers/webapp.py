from typing import Annotated
from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from starlette import status

from app.schemas import UserForm
import db

router = APIRouter(prefix="", tags=["webapp"])
templates = Jinja2Templates(directory="src/app/templates")


@router.get("/")
async def index(request: Request):
    return templates.TemplateResponse("home", context={"request": request})


@router.get("/conversation")
async def conversation(request: Request):
    return templates.TemplateResponse("conversation", context={"request": request})


@router.get("/user/add")
async def add_user_form(request: Request):
    return templates.TemplateResponse("add_user_form", context={"request": request})


@router.post("/user/add")
async def add_user_form_post(
    request: Request,
    user_repo: Annotated[db.UserRepository, Depends(db.UserRepository)],
    uf: UserForm = Depends(UserForm),
):
    dbUser = db.User(fname=uf.fname, lname=uf.lname, phone=uf.phone)
    new_user = user_repo.insert(dbUser)
    return RedirectResponse(
        url="/user?sel_user=" + str(new_user.id) + "", status_code=status.HTTP_302_FOUND
    )


@router.get("/user")
async def list_users(
    user_repo: Annotated[db.UserRepository, Depends(db.UserRepository)],
    request: Request,
    sel_user: int = 0,
):
    users = user_repo.get_all()
    return templates.TemplateResponse(
        "list_users",
        context={
            "request": request,
            "users": users,
            "sel_user": sel_user,
        },
    )
