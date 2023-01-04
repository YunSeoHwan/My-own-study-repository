import sys
input = sys.stdin.readline

# 회의목록
meet = []

n = int(input())

# 회의시간 입력받음
for i in range(n):
    meet.append(list(map(int, input().split())))

# 끝나는 시간순으로 정렬후, 동일경우 시간시간 순으로 정렬
meet.sort(key = lambda x: (x[1], x[0]))

# 끝나는 시간
end = meet[0][1]

# 회의 횟수
cnt = 1

# 회의끝나는 시간보다 같거나 큰 부분만 고려
for i in range(1, n):
    if end <= meet[i][0]:
        end = meet[i][1]
        cnt+=1
        
print(cnt)