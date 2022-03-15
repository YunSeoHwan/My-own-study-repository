hour, min = map(int, input().split())
time = int(input())

new_min = min + time

if new_min < 60:
    print(hour, new_min)
elif new_min >= 60:
    hour += (new_min // 60)
    if hour >= 24:
        hour -= 24
    new_min = new_min % 60
    print(hour, new_min)

    