from fastapi import APIRouter
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.staticfiles import StaticFiles


router = APIRouter()

templates = Jinja2Templates(directory="templates/")



# 지역 상세내용 페이지
## 서울
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

## 부산
@router.post("/info_Busan")
async def info_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="detailed_region/info_Busan.html", context={'request':request})

@router.get("/info_Busan")
async def info_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="detailed_region/info_Busan.html", context={'request':request})

## 강원도
@router.post("/info_Gangwondo")
async def info_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="detailed_region/info_Gangwondo.html", context={'request':request})

@router.get("/info_Gangwondo")
async def info_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="detailed_region/info_Gangwondo.html", context={'request':request})

## 제주도
@router.post("/info_Jeju")
async def info_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="detailed_region/info_Jeju.html", context={'request':request})

@router.get("/info_Jeju")
async def info_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="detailed_region/info_Jeju.html", context={'request':request})

## 인천
@router.post("/info_Incheon")
async def info_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="detailed_region/info_Incheon.html", context={'request':request})

@router.get("/info_Incheon")
async def info_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="detailed_region/info_Incheon.html", context={'request':request})