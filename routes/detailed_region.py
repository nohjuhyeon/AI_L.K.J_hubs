from fastapi import APIRouter
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.staticfiles import StaticFiles


router = APIRouter()

templates = Jinja2Templates(directory="templates/")



## 지역 상세내용 페이지
@router.post("/info_Seoul")
async def info_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="detailed_region/info_Seoul.html", context={'request':request})

@router.get("/info_Seoul")
async def info_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="detailed_region/info_Seoul.html", context={'request':request})