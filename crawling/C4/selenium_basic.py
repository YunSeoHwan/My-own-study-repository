from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

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