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
    dict_region={'서울':0, '경기':0, '인천':0, '강원':0, '경남':0, '경북':0, '광주':0, '대구':0, '대전':0,
                   '부산':0, '세종':0, '울산':0, '전남':0, '전북':0, '충남':0, '충북':0, '제주':0}
    try:
        std_month = int(dict(request._query_params)['month'])
    except:
        std_month = 3
    visitor_conditions = {"std_month" : std_month,"destination_type" : { '$regex': '전체'}}
    visitor_dict = await collection_data_concept_search.getsbyconditions(visitor_conditions)
    visitor_dict = [module.dict() for module in visitor_dict]
    for i in range(len(visitor_dict)):
        dict_region[visitor_dict[i]['region']] = dict_region[visitor_dict[i]['region']] + visitor_dict[i]['destination_search']
    dict_region = dict(sorted(dict_region.items(), key=lambda x: x[1], reverse=True))
    region_list = list(dict_region.keys())[:5]
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

