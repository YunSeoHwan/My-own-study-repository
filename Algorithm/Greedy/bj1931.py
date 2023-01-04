import sys
input = sys.stdin.readline

meet = []

n = int(input())
for i in range(n):
    meet.append(list(map(int, input().split())))
meet.sort(key = lambda x: (x[1], x[0]))
end = meet[0][1]
i = 1
cnt = 1

for i in range(1, n):
    if end <= meet[i][0]:
        end = meet[i][1]
        cnt+=1
print(cnt)