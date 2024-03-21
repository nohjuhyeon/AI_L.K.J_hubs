from fastapi import APIRouter
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.staticfiles import StaticFiles
from databases.connections import Database
from models.attraction_search_info import attraction_search_info
from models.season_concept_info import season_concept_info
from models.data_chart import data_concept_search
collection_data_concept_search=Database(data_concept_search)
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
    print(dict(request._query_params))

    try:
        std_month = dict(request._query_params)['month']
    except:
        std_month = '3'
    region_dict ={'1' : ['서울', '부산', '인천','울산','대구'],
                  '2' : ['서울', '제주', '부산','인천','강원'],
                  '3' : ['서울', '세종', '경기','인천','광주'],
                  '4' : ['충남', '경기', '세종','충북','전남'],
                  '5' : ['전북', '충북', '충남','전남','경기'],
                  '6' : ['충북', '강원', '제주','광주','충남'],
                  '7' : ['강원', '충북', '제주','경북','부산'],
                  '8' : ['강원', '전남', '경북','제주','경남'],
                  '9' : ['충남', '인천', '충북','전북','경기'],
                  '10' :['충북', '경북', '전북','충남','전남'],
                  '11' : ['충북', '대전', '대구','광주','전북'],
                  '12월' : ['서울', '대구', '대전','광주','부산']}
    region_list = region_dict[std_month]
    return templates.TemplateResponse(name="event/best_region.html", context={'request':request, 'region_list':region_list})

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
        if len(season_list) == 0:
            attraction_list = []
        else:
            conditions = {}
            attraction_list = await collection_attraction.getsbyconditions(conditions)
            attraction_list = [module.dict() for module in attraction_list]
            attraction_list = sorted(attraction_list, key=lambda x: x['attraction_search'], reverse=True)

    elif len(concept_list) == 0 and len(region_list) != 0:
        conditions = {"region" : { '$in': region_list}}
        attraction_list = await collection_attraction.getsbyconditions(conditions)
        attraction_list = [module.dict() for module in attraction_list]
        attraction_list = sorted(attraction_list, key=lambda x: x['attraction_search'], reverse=True)
    elif len(concept_list) != 0 and len(region_list) == 0:
        conditions = {"destination_type" : { '$in': concept_list}}
        attraction_list = await collection_attraction.getsbyconditions(conditions)
        attraction_list = [module.dict() for module in attraction_list]
        attraction_list = sorted(attraction_list, key=lambda x: x['attraction_search'], reverse=True)
    else:
        conditions = {"region" : { '$in': region_list},"destination_type" : { '$in': concept_list}}
        attraction_list = await collection_attraction.getsbyconditions(conditions)
        attraction_list = [module.dict() for module in attraction_list]
        attraction_list = sorted(attraction_list, key=lambda x: x['attraction_search'], reverse=True)
    # print(search_word)
    return templates.TemplateResponse(name="event/recommend_region.html", context={'request':request,'attraction_list':attraction_list})

