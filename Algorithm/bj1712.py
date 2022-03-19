a, b, c = map(int, input().split())

if b>=c:
    print(-1)
else:
    print(int(a/(c-b)+1))   # 방정식으로 접근해보기 x 값 찾기