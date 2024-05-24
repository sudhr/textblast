from typing import Annotated, List

import tb_storage
from app.schemas.user import UserForm
from fastapi import APIRouter, Depends, File, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from starlette import status

from ..schemas.campaign import NewCampaignForm

router = APIRouter(prefix="", tags=["webapp"])
templates = Jinja2Templates(directory="src/app/templates")


#
# Jinja2 filters
#
def datetime_format(value, format="%Y-%m-%d %H:%M:%S"):
    return value.strftime(format)


templates.env.filters["datetime_format"] = datetime_format


@router.get("/")
async def index(request: Request):
    return templates.TemplateResponse("home", context={"request": request})


#
# User
#


@router.get("/user/add")
async def add_user_form(request: Request):
    return templates.TemplateResponse("add_user_form", context={"request": request})


@router.post("/user/add")
async def add_user_form_post(
    request: Request,
    user_repo: Annotated[tb_storage.UserRepository, Depends(tb_storage.UserRepository)],
    uf: UserForm = Depends(UserForm),
):
    dbUser = tb_storage.User(fname=uf.fname, lname=uf.lname, phone=uf.phone)
    # try:
    new_user = user_repo.insert(dbUser)
    return RedirectResponse(
        url="/user?sel_user=" + str(new_user.id) + "",
        status_code=status.HTTP_302_FOUND,
    )
    # except Exception as e:
    #     print(e)


@router.get("/user")
async def list_users(
    user_repo: Annotated[tb_storage.UserRepository, Depends(tb_storage.UserRepository)],
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


#
# Campaigns
#


@router.get("/campaign")
async def list_campaigns(
    request: Request,
    campaign_repo: Annotated[
        tb_storage.CampaignRepository, Depends(tb_storage.CampaignRepository)
    ],
):
    campaigns: List[tb_storage.Campaign] = campaign_repo.get_all()
    return templates.TemplateResponse(
        "campaign/list_campaigns", context={"request": request, "campaigns": campaigns}
    )


@router.get("/campaign/new")
async def new_campaign_form(request: Request):
    return templates.TemplateResponse(
        "campaign/new_campaign_form", context={"request": request}
    )


@router.post("/campaign/new")
async def new_campaign_form_post(
    request: Request,
    campaign_repo: Annotated[
        tb_storage.CampaignRepository, Depends(tb_storage.CampaignRepository)
    ],
    csv_file: Annotated[bytes, File()],
    ncf: NewCampaignForm = Depends(NewCampaignForm),
):
    # Create entry in the database
    ncam: tb_storage.Campaign = tb_storage.Campaign(
        name=ncf.name,
        description=ncf.description,
        start_date=ncf.start_time,
        end_date=ncf.end_time,
    )
    cam = campaign_repo.insert(ncam)
    # Parse the CSV file

    return RedirectResponse(
        url=f"/campaign/{cam.id}", status_code=status.HTTP_302_FOUND
    )


@router.get("/campaign/{campaign_id}")
async def show_campaign(
    request: Request,
    campaign_repo: Annotated[
        tb_storage.CampaignRepository, Depends(tb_storage.CampaignRepository)
    ],
    campaign_id: int,
):
    campaign = campaign_repo.get_by_id(campaign_id)
    if campaign is not None:
        return templates.TemplateResponse(
            "campaign/show_campaign", context={"request": request, "campaign": campaign}
        )
    else:
        return templates.TemplateResponse(
            "error",
            context={
                "request": request,
                "exc": "Campaign not found",
            },
            status_code=status.HTTP_400_BAD_REQUEST,
        )


#
# Conversation
#


@router.get("/conversation")
async def conversation_lookup(request: Request):
    return templates.TemplateResponse(
        "conversation/lookup", context={"request": request}
    )
