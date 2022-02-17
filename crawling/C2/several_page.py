import requests
from bs4 import BeautifulSoup
import pyautogui

keyword = pyautogui.prompt("검색어를 입력하세요.")
lastpage = pyautogui.prompt("마지막 페이지 번호를 입력하세요.")
pageNum = 1
for i in range(1, int(lastpage) * 10, 10):
    print(f"{pageNum} 페이지 입니다. =============================")
    response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}&start={i}")
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.select(".news_tit")    # 결과가 list로 나옴

    for link in links:
        title = link.text   # 태그 안에 텍스트요소 리턴
        url = link.attrs['href']    # href 요소 리턴 -> attrs는 []안 속성값을 가져옴
        print(title, url)
    pageNum += 1