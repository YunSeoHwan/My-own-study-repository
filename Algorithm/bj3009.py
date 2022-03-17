x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

x4 = 0
y4 = 0

if x1 == x2:
    x4 += x3

if x2 == x3:
    x4 += x1

if x1 == x3:
    x4 += x2

if y1 == y2:
    y4 += y3

if y2 == y3:
    y4 += y1

if y1 == y3:
    y4 += y2

print(x4, y4)

# 좋은 풀이법
x_ = []
y_ = []
for i in range(3):
        x, y = map(int, input().split())
        x_.append(x)
        y_.append(y)
for i in range(3):
        if x_.count(x_[i]) == 1:
                x = x_[i]
        if y_.count(y_[i]) == 1:
                y = y_[i]
print(x, y)