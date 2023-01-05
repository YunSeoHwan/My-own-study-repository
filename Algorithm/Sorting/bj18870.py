import sys

input = sys.stdin.readline
n = int(input())

# 좌표값 입력받기
grid = list(map(int, input().split()))

# 집합으로 만든 뒤, 정렬
sort_grid = sorted(list(set(grid)))

# 해당 index가 압축된 값
dict = {sort_grid[i] : i  for i in range(len(sort_grid))}

# 해당하는 값의 value 출력
for i in grid:
    print(dict[i], end=" ")

# import sys

# input = sys.stdin.readline
# n = int(input())

# grid = list(map(int, input().split()))
# sort_grid = sorted(list(set(grid)))
    
# press = []
# for i in grid:
#     index = sort_grid.index(i)
#     press.append(index)

# for i in press:
#     print(i, end=" ")