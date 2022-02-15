import requests

reponse = requests.get('https://www.naver.com')
html = reponse.text # 굉장히 중요함. text는 html 코드를 반환함
print(html)