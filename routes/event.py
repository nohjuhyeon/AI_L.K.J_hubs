from fastapi import APIRouter
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.staticfiles import StaticFiles
from databases.connections import Database
from models.attraction_search_info import attraction_search_info
from models.season_concept_info import season_concept_info
collection_attraction = Database(attraction_search_info)
collection_season_concept = Database(season_concept_info)

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
    concept_list = []
    region_list =[]
    season_list=[]
    for i in range(len(list( dict(request._query_params).keys()))):
        if list( dict(request._query_params).keys())[i][0:7] == 'concept':
            concept_list.append(list( dict(request._query_params).values())[i]) 
        elif list( dict(request._query_params).keys())[i][0:6] == 'season':
            season_list.append(list( dict(request._query_params).values())[i]) 
        elif list( dict(request._query_params).keys())[i][0:6] == 'region':
            region_list.append(list( dict(request._query_params).values())[i]) 
    if len(concept_list) == 0 and len(region_list) == 0:
        conditions = {}
    elif len(concept_list) != 0 and len(region_list) == 0:
        conditions = {"region" : { '$in': region_list}}

    attraction_list = await collection_attraction.getsbyconditions(conditions)
    attraction_list = [module.dict() for module in attraction_list]
    attraction_list = sorted(attraction_list, key=lambda x: x['attraction_search'], reverse=True)
    attraction_list=[]
    # print(search_word)
    return templates.TemplateResponse(name="event/recommend_region.html", context={'request':request,'attraction_list':attraction_list})

