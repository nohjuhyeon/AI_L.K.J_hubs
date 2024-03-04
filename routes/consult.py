from fastapi import APIRouter
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from databases.connections import Database
from models.admin_notice import Admin_notice_list
collection_admin_notice_list = Database(Admin_notice_list)


router = APIRouter()

templates = Jinja2Templates(directory="templates/")



## 공지 사항
@router.post("/user_notice") # 펑션 호출 방식
async def list_post(request:Request):
    notices = await collection_admin_notice_list.get_all()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="consult/user_notice.html", context={'request':request, "notices": notices})

@router.get("/user_notice") # 펑션 호출 방식
async def list_post(request:Request):
    notices = await collection_admin_notice_list.get_all()
    print(dict(await request.form()))
    return templates.TemplateResponse("consult/user_notice.html" , context={"request": request, "notices": notices} )

