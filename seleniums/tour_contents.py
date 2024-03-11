## dbmongo의 collection 연결
from pymongo import MongoClient
mongoClient = MongoClient("mongodb://192.168.10.240:27017")
# database 연결
database = mongoClient["AI_LKJ"]
# collection 작업
collection = database['tour_contents']
collection.delete_many({})


# * 웹 크롤링 동작
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
# Chrome 브라우저 옵션 생성
chrome_options = Options()
# User-Agent 설정
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")
from webdriver_manager.chrome import ChromeDriverManager
webdriver_manager_directory = ChromeDriverManager().install()
# WebDriver 생성
browser = webdriver.Chrome(service = ChromeService(webdriver_manager_directory), options=chrome_options)                        # - chrome browser 열기
# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

pass
browser.get("https://travel.naver.com/domestic/01/guide/all")                                     # - 주소 입력

                                                    # - 가능 여부에 대한 OK 받음
pass
html = browser.page_source                          # - html 파일 받음(and 확인)
# print(html)

from selenium.webdriver.common.by import By          # - 정보 획득
from selenium.webdriver.common.keys import Keys
import time

# 돋보기
search_button = "div.header_sub__z2ac0 > button"
element_search = browser.find_element(by=By.CSS_SELECTOR, value=search_button)


#더보기 버튼
more_button = "div > div > main > div> div.guide_GuidePanel__hO6Rf > div > div > button"
element_more = browser.find_element(by=By.CSS_SELECTOR, value=more_button)

# 리뷰 제목
review_title = "b.guide_name__OKy4W.expandableText_EllipsisText__gaduJ"
element_review = browser.find_elements(by=By.CSS_SELECTOR, value=review_title)



element_search.click()
time.sleep(1)

# 지역
region_button = "div.searchbox_svc_tabs__MkKLI > a.searchbox_svc_tab__kjMI2"
element_region = browser.find_elements(by=By.CSS_SELECTOR, value=region_button)

# 세부지역
detail_region_button = "div.searchbox_svc_PanelItem__nQUao.as_domestic > a"
element_detail = browser.find_element(by=By.CSS_SELECTOR, value=detail_region_button)

# 여행컨텐츠 버튼
contents_button = "nav > div > a:nth-child(2)"
element_contents = browser.find_element(by=By.CSS_SELECTOR, value=contents_button)

for x in range(6,18):
    element_region[x].click()
    time.sleep(1)
    element_detail.click()
    time.sleep(2)
    element_contents.click()
    time.sleep(1)   

# while True:
    for y in range(5):
        # 더보기 버튼을 찾아 클릭
        element_more.click()
        time.sleep(1)

    list_review = []
    for z in range(len(element_review)):
        review_text = element_review[z].text
        list_review.append(review_text)
print(list_review)

    # # MongoDB에 댓글 저장
    # collection.insert_one({"": author, "content": content, "rating": rating})

        # 더보기 버튼이 없으면 빈 리스트에 리뷰 제목들을 추가
        


# while True:
# # for i in range(3):
#     element_body.send_keys(Keys.END)
#     current_scrollHeight = browser.execute_script("return document.body.scrollHeight")
#     if previous_scrollHeight >= current_scrollHeight:
#         break
#     else:
#         previous_scrollHeight = current_scrollHeight
#     time.sleep(3)
# pass
# user_list = element_body.find_elements(by=By.CSS_SELECTOR,value = "div.css-13j4ly.egj9y8a4")
# user_name_list = []
# grade_list = []
# content_list = []
# for user_item in user_list:
#     try:
#         user_name = user_item.find_element(by=By.CSS_SELECTOR,value = "div.css-drz8qh.egj9y8a2")                    # 작성자 정보 추출
#         str_user_name = user_name.text
#     except: 
#         str_user_name = ""
#     user_name_list.append(str_user_name)
#     try:
#         grade = user_item.find_element(by=By.CSS_SELECTOR,value = "div.css-31ods0.egj9y8a0")                        # 별점 점수 정보 추출
#         str_grade = grade.text
#     except:
#         str_grade = ""
#     grade_list.append(str_grade)
#     try:
#         content = user_item.find_element(by=By.CSS_SELECTOR,value = "div.css-2occzs.egj9y8a1")                      # 내용 정보 추출                                                                             # 데이터 데이스에 정보 전달
#         str_content = content.text
#     except:
#         str_content = ""
#     content_list.append(str_content)
# for i in range(len(user_list)):
#     collection.insert_one({"작성자": user_name_list[i],                                                         
#                             "별점 점수": grade_list[i],
#                             "내용": content_list[i]})

pass
browser.quit()                                      # - 브라우저 종료

# 작성자: div.css-drz8qh.egj9y8a2
# 별점: div.css-31ods0.egj9y8a0
# 내용: div.css-2occzs.egj9y8a1