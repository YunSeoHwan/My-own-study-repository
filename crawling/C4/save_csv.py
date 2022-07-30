from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv

# 브라우저 생성
browser = webdriver.Chrome('C:/chromedriver.exe')

# 웹사이트 열기
browser.get('https://www.naver.com')
browser.implicitly_wait(10)     # 로딩이 끝날때까지 10초까지 기다려줌

# 쇼핑메뉴 클릭하기
browser.find_element(By.CSS_SELECTOR, 'a.nav.shop').click()
time.sleep(2)

# 검색창 클릭
search = browser.find_element(By.CSS_SELECTOR, 'input._searchInput_search_input_QXUFf')
search.click()

# 검색어 입력 
search.send_keys('아이폰 13')
search.send_keys(Keys.ENTER)

# 무한 스크롤

# 스크롤 전 높이
before_h = browser.execute_script("return window.scrollY")

while True:
    # 맨 아래로 스크롤 내리기
    browser.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.END)

    # 스크롤 사이 페이지 로딩시간
    time.sleep(1)

    # 스크롤 후 높이
    after_h = browser.execute_script('return window.scrollY')

    if after_h == before_h:
        break
    before_h = after_h

# 파일 생성
f = open(r'C:\python_crawling\C4\data.csv', 'w', encoding='CP949', newline='')
csvWriter = csv.writer(f)

# 상품 정보 div
items = browser.find_elements(By.CSS_SELECTOR, '.basicList_info_area__17Xyo')

for item in items:
    name = item.find_element(By.CSS_SELECTOR, '.basicList_title__3P9Q7').text
    try:
        price = item.find_element(By.CSS_SELECTOR, '.price_num__2WUXn').text
    except:
        price = "판매중단"
    link = item.find_element(By.CSS_SELECTOR, '.basicList_title__3P9Q7 > a').get_attribute('href')
    # 데이터 쓰기
    csvWriter.writerow([name, price, link])

f.close()