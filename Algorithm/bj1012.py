import sys
num = int(input())
sys.setrecursionlimit(10000)
def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if array[x][y] == 1:
        array[x][y] = 0
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

# 배추밭 생성
for i in range(num):
    m, n, k = map(int, sys.stdin.readline().split())
    array = [[0] * m for _ in range(n)]

    # 지렁이 위치 삽입
    for j in range(k):
        a, b = map(int, sys.stdin.readline().split())
        array[b][a] = 1
    result = 0
    for i in range(n):
        for j in range(m):
            if array[i][j] == 1:
                if dfs(i, j) == True:
                    result +=1
    
    print(result)