from fastapi import APIRouter
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.staticfiles import StaticFiles


router = APIRouter()

templates = Jinja2Templates(directory="templates/")

## 베스트 여행지
@router.post("/best_region") # 펑션 호출 방식
async def list_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="event/best_region.html", context={'request':request})

@router.get("/best_region") # 펑션 호출 방식
async def list_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="event/best_region.html", context={'request':request})

## 베스트 숙소
@router.post("/best_dorm") # 펑션 호출 방식
async def list_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="event/best_dorm.html", context={'request':request})

@router.get("/best_dorm") # 펑션 호출 방식
async def list_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="event/best_dorm.html", context={'request':request})

