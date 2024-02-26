from fastapi import APIRouter
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request


router = APIRouter()

templates = Jinja2Templates(directory="templates/")

## 메인
@router.post("/") # 펑션 호출 방식
async def list_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="admin/admin_main.html", context={'request':request})

@router.get("/") # 펑션 호출 방식
async def list_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="admin/admin_main.html", context={'request':request})

## 관리자 로그인 
@router.post("/admin_login")
async def list_post(request:Request) :
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="admin/admin_login.html", context={'request':request})

@router.get("/admin_login")
async def list_post(request:Request) :
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="admin/admin_login.html", context={'request':request})

## 공지 관리
@router.post("/notice") # 펑션 호출 방식
async def list_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="admin/admin_notice.html", context={'request':request})

@router.get("/notice") # 펑션 호출 방식
async def list_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="admin/admin_notice.html", context={'request':request})

## 내용 관리
@router.post("/contents") # 펑션 호출 방식
async def list_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="admin/admin_contents.html", context={'request':request})

@router.get("/contents") # 펑션 호출 방식
async def list_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="admin/admin_contents.html", context={'request':request})


## 회원 관리
@router.post("/users") # 펑션 호출 방식
async def list_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="admin/admin_users.html", context={'request':request})

@router.get("/users") # 펑션 호출 방식
async def list_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="admin/admin_users.html", context={'request':request})
