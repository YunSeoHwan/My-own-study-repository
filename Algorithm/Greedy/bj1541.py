import sys

input = sys.stdin.readline

s = list(input().split('-'))

result = 0

# 첫 항목의 값을 저장함(무조건 +) -> +와 붙어서 저장되어 있으므로 분해
for i in s[0].split('+'):
    result += int(i)

# 나머지 항목 카운팅(- 기준으로 끊었기때문에 뒤 항목은 전부 뺌)
for i in s[1:]:

    # +와 붙어 있는 항목은 쪼개서 빼줌
    for j in i.split('+'):
        result -= int(j)

print(result)