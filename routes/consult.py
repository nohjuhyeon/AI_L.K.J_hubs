from fastapi import APIRouter
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from databases.connections import Database
from fastapi import HTTPException
from beanie import PydanticObjectId
import requests

router = APIRouter()

templates = Jinja2Templates(directory="templates/")


from models.admin_notice import Admin_notice_list
collection_admin_notice_list = Database(Admin_notice_list)
from models.one_on_one_CS import One_on_one_CS_list
One_on_one_CS_list = Database(One_on_one_CS_list)
from models.data_chart import data_attraction, data_concept_search, data_consume,data_consume_transition,data_trend_search
collection_data_attraction=Database(data_attraction)
collection_data_concept_search=Database(data_concept_search)
collection_data_consume=Database(data_consume)
collection_data_consume_transition=Database(data_consume_transition)
collection_data_trend_search=Database(data_trend_search)

from models.frequent_CS import FAQ_list
collection_FAQ_list = Database(FAQ_list)

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

## 자주 묻는 질문 페이지
@router.post("/frequent_CS")
async def frequent_cs_post(request:Request):
    form_data = await request.form()
    print(dict(form_data))
    faqs = await collection_FAQ_list.get_all()
    return templates.TemplateResponse(name="consult/frequent_CS.html", context={'request':request, 'faqs':faqs})

@router.get("/frequent_CS")
async def frequent_cs_get(request:Request):
    faqs = await collection_FAQ_list.get_all()
    return templates.TemplateResponse(name="consult/frequent_CS.html", context={'request':request, 'faqs':faqs})

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
@router.get("/one_on_one_add")
async def get_one_on_one(request: Request):
    qna = await One_on_one_CS_list.get_all()
    return templates.TemplateResponse("consult/one_on_one_CS_main.html", context={'request':request, 'qna': qna})

@router.post("/one_on_one_add")
async def add_one_on_one(request: Request):
    qna_dict = dict(await request.form())
    add_qna = One_on_one_CS_list(**qna_dict)
    await One_on_one_CS_list.save(add_qna)
    return {"success": True}

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
    region_list = ['강원', '경기', '경남', '경북', '광주', '대구', '대전', '부산', '서울', '세종', '울산', '인천', '전남', '전북', '제주', '충남', '충북']
    await request.form()
    print(dict(await request.form()))

    # 월별 방문객 수 
    visitor_conditions = {"destination_type" : { '$regex': '전체'}}
    visitor_list = await collection_data_concept_search.getsbyconditions(visitor_conditions)
    visitor_list = [module.dict() for module in visitor_list]
    dict_visitor = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0,'11':0,'12':0}
    for i in range(len(visitor_list)):
        if visitor_list[i]['region'] == region_list[5]:
            dict_visitor[str(visitor_list[i]['std_month'])] = dict_visitor[str(visitor_list[i]['std_month'])]  + visitor_list[i]['destination_search']/40000

    # 유형별 목적지 검색량
    concept_conditions = {"destination_type": { "$ne": "전체" }}
    dict_concept={'숙박':0, '음식':0, '기타관광':0, '쇼핑':0, '문화관광':0, '역사관광':0, '자연관광':0, '체험관광':0, '레저스포츠':0}
    concept_list = await collection_data_concept_search.getsbyconditions(concept_conditions)
    concept_list = [module.dict() for module in concept_list]
    for i in range(len(concept_list)):
        dict_concept[concept_list[i]["destination_type"]] = dict_concept[concept_list[i]["destination_type"]] +  concept_list[i]['destination_search']/40000

    # 월별 관광 소비 추이 이거
    consume_transition = {"destination_type" : { '$regex': '전체'}}
    consume_transition_list = await collection_data_consume_transition.getsbyconditions(consume_transition)
    consume_transition_list = [module.dict() for module in consume_transition_list]
    dict_consume_transition = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0,'11':0,'12':0}
    for i in range(len(consume_transition_list)):
        if consume_transition_list[i]['region'] == consume_transition_list[5]:
            dict_consume_transition[str(consume_transition_list[i]['std_month'])] = dict_consume_transition[str(consume_transition_list[i]['std_month'])]  + consume_transition_list[i]['destination_search']/40000
    
    # 월별 키워드 검색량
    trend_list = await collection_data_trend_search.get_all()
    trend_list = [module.dict() for module in trend_list]
    tour_trend_column = ['레포츠', '휴식/힐링', '기타', '미식', '체험']
    list_month_trend = [{'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0,'11':0,'12':0},
                        {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0,'11':0,'12':0},
                        {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0,'11':0,'12':0},
                        {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0,'11':0,'12':0},
                        {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0,'11':0,'12':0}]
    for j in range(len(trend_list)):
        list_month_trend[tour_trend_column.index(trend_list[j]['tour_trend'])][str(trend_list[j]['std_month'])] =list_month_trend[tour_trend_column.index(trend_list[j]['tour_trend'])][str(trend_list[j]['std_month'])] + trend_list[j]['num_mention']
        pass
    
    # 관광소비 유형
    dict_consume={'쇼핑업':0, '숙박업':0, '식음료업':0, '여가서비스업':0, '여행업':0, '운송업':0}
    consume_list = await collection_data_consume.get_all()
    consume_list = [module.dict() for module in consume_list]
    for i in range(len(consume_list)):
        dict_consume[consume_list[i]["industry_major_cate"]] = dict_consume[consume_list[i]["industry_major_cate"]] +  consume_list[i]['consumption_amount']/40000

    return templates.TemplateResponse(name="consult/data_chart.html", context={'request':request, 'dict_visitor':dict_visitor,'dict_concept':dict_concept,'list_month_trend':list_month_trend,'consume_list':consume_list})