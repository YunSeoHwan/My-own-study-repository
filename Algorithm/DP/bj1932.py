import sys

n = int(sys.stdin.readline())
tree = []
for _ in range(n):
    tree.append(list(map(int, sys.stdin.readline().split())))

# 각 항목에 올수있는 경우 합으로 저장
for i in range(1,n):
    
    # 1행일 때 0,1가지므로 2개 값 필요
    for j in range(0,i+1):
        
        # 왼쪽 끝인 경우
        if j == 0:
            tree[i][j] = tree[i-1][j] + tree[i][j]

        # 오른쪽 끝인 경우
        elif i == j:
            tree[i][j] = tree[i-1][j-1] + tree[i][j]
        
        # 2개의 경로중 큰 값으로 합 저장
        else:
            tree[i][j] = max(tree[i][j] + tree[i-1][j-1], tree[i][j] + tree[i-1][j])

# 각 행에서 가장 큰 값 출력
print(max(tree[n-1]))
