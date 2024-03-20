from fastapi import APIRouter
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.staticfiles import StaticFiles
from databases.connections import Database
from models.attraction_search_info import attraction_search_info
collection_attraction = Database(attraction_search_info)

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

## 관광지 추천
@router.post("/recommend_region") # 펑션 호출 방식
async def list_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="event/recommend_region.html", context={'request':request})

@router.get("/recommend_region") # 펑션 호출 방식
async def list_post(request:Request):
    dict(request._query_params)
    conditions={}
    attraction_list = collection_attraction.getsbyconditions(conditions)
    print(dict(request._query_params))
    return templates.TemplateResponse(name="event/recommend_region.html", context={'request':request,'attraction_list':attraction_list})

