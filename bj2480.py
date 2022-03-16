d1, d2, d3 = map(int, input().split())  # 주사위 변수

if d1==d2==d3:
    print(d1*1000 + 10000)
elif d1==d2:
    print(d1*100 + 1000)
elif d1==d3:
    print(d1*100 + 1000)
elif d2==d3:
    print(d2*100 + 1000)
else:
    print(max(d1, d2, d3)*100)