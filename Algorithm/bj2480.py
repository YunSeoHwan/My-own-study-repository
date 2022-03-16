d1, d2, d3 = map(int, input().split())  # 주사위 변수

if d1==d2==d3:                  # 전부 같을 때
    print(d1*1000 + 10000)
elif d1==d2:                    # d1, d2가 같을 때
    print(d1*100 + 1000)
elif d1==d3:                    # d1, d3가 같을 때
    print(d1*100 + 1000)
elif d2==d3:                    # d2, d3가 같을 때
    print(d2*100 + 1000)
else:                           # 전부 다를 때
    print(max(d1, d2, d3)*100)
