n = int(input())
user = []
for i in range(n):
    age, name = map(str, input().split())
    age = int(age)
    user.append((age, name))

# 첫 번째 index만 정렬
user.sort(key=lambda x: x[0])

for i in user:
    print(i[0], i[1])