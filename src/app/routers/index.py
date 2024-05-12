from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="src/app/templates")


@router.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", context={"request": request})
