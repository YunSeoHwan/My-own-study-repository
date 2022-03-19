x, y, w, h = map(int, input().split())
print(min(x, y , w-x, h-y))

# 직사각형 내부 한점에서 가장 가까운 값을 구하면 됨으로 최솟값을 구함