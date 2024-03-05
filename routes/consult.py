from fastapi import APIRouter
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from databases.connections import Database
from fastapi import HTTPException
import requests
from models.admin_notice import Admin_notice_list
collection_admin_notice_list = Database(Admin_notice_list)
from models.one_on_one_CS import One_on_one_CS_list
One_on_one_CS_list = Database(One_on_one_CS_list)


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

## 1대1 문의 메인페이지
@router.post("/one_on_one_CS_main") # 펑션 호출 방식
async def list_post(request:Request):
    qna = await One_on_one_CS_list.get_all()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="consult/one_on_one_CS_main.html", context={'request':request, "qnas": qna})

@router.get("/one_on_one_CS_main") # 펑션 호출 방식
async def list_post(request:Request):
    qna = await One_on_one_CS_list.get_all()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="consult/one_on_one_CS_main.html", context={'request':request, "qnas": qna})

## 1대1 문의 페이지
@router.post("/one_on_one_CS") # 펑션 호출 방식
async def list_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="consult/one_on_one_CS.html", context={'request':request})

@router.get("/one_on_one_CS") # 펑션 호출 방식
async def list_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="consult/one_on_one_CS.html", context={'request':request})

## 새로운 1대1 질문 추가
@router.post("/one_on_one_add")
async def add_one_on_one(request : Request):
    qna_dict = dict(await request.form())
    add_qna = One_on_one_CS_list(**qna_dict)
    await One_on_one_CS_list.save(add_qna)
    qna = await One_on_one_CS_list.get_all()
    return templates.TemplateResponse("consult/one_on_one_CS_main.html", context={'request':request, 'qna': qna})

## 카카오톡 상담
@router.post("/kakaotalk_CS")
@router.get("/kakaotalk_CS")
async def kakaotalk_CS(request: Request):
    access_token = "Kuah5OooBvqo_gpRWE075RorCj1vn8ZYkucKKwynAAABjgy4pJ-oblpFv_zasg"  # 실제 액세스 토큰으로 바꿔주세요

    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get("https://kapi.kakao.com/v2/api/talk/memo/default/send", headers=headers)

    return templates.TemplateResponse("template.html", context={'request':request, 'response': response.json()})



## 데이터 현황 차트
@router.post("/data_chart") # 펑션 호출 방식
async def list_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="consult/data_chart.html", context={'request':request})

@router.get("/data_chart") # 펑션 호출 방식
async def list_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="consult/data_chart.html", context={'request':request})