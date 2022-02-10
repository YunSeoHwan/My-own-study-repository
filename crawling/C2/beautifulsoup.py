import requests
from bs4 import BeautifulSoup

reponse = requests.get('https://www.naver.com')
html = reponse.text
soup = BeautifulSoup(html, 'html.parser')
word = soup.select_one('#NM_set_home_btn')

print(word)         # 해당 태그 전체 값
print(word.text)    # 해당 값의 요소만 가져옴