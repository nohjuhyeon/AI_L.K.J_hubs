from fastapi import APIRouter
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request


router = APIRouter()

templates = Jinja2Templates(directory="templates/")

from models.admin_notice import Admin_notice_list
from databases.connections import Database
collection_admin_notice_list = Database(Admin_notice_list)


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
    # MongoDB에서 공지사항 데이터 가져오기
    notices = await collection_admin_notice_list.get_all() # 메서드를 사용하여 모든 공지사항을 가져옴
    # print(notices)
    # 템플릿에 데이터 전달하여 HTML 페이지 렌더링
    return templates.TemplateResponse("amin/admin_notice.html" , context={"request": request, "notices": notices} )


@router.get("/notice") # 펑션 호출 방식
async def list_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    notices = await collection_admin_notice_list.get_all() # 메서드를 사용하여 모든 공지사항을 가져옴
    # print(notices)
    return templates.TemplateResponse(name="admin/admin_notice.html", context={'request':request, 'notices': notices})

## 공지사항 내용 보기
@router.get("/admin_notice_content/{object_id}")
async def get_notice_content(request : Request,object_id) :
    # notice_id를 기반으로 데이터베이스에서 공지사항 내용을 가져옴
    notices = await collection_admin_notice_list.get({"_id" : object_id})
    print(notices)
    return templates.TemplateResponse(name="admin/admin_notice_content.html", context={'request' : request, 'content' : notices})

@router.post("/admin_notice_content/{object_id}")
async def post_notice_content(request : Request,object_id) :
    # notice_id를 기반으로 데이터베이스에서 공지사항 내용을 가져옴
    notices = await collection_admin_notice_list.get({"_id" : object_id})
    print(notices)
    return templates.TemplateResponse(name="admin/admin_notice_content.html", context={'request' : request, 'content' : notices})

## 공지사항 글쓰기
@router.get("/admin_notice_write")
async def get_notice_write(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="admin/admin_notice_write.html", context={'request':request})

@router.post("/admin_notice_write")
async def post_notice_write(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="admin/admin_notice_write.html", context={'request':request})

## 게시물 내용 관리
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

# 


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
