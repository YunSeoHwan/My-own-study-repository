import sys
# set 자료형은 list를 정렬하는것보다 시간이 덜 든다.
n = int(sys.stdin.readline())
n_list = set(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))
for i in m_list:
    if i in n_list:
        print(1)
    else:
        print(0)