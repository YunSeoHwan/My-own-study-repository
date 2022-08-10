import sys

n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))

# index를 담을 dict 생성
dict = {}

# n_list 개수를 dict에 할당
for i in n_list:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

# m_list 값이 dict에 있으면 그때의 index출력
for i in m_list:
    if i in dict:
        print(dict[i], end=" ")
    else:
        print(0, end=" ")