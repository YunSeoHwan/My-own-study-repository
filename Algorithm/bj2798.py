num, main_number = map(int, input().split())

num_list = list(map(int, input().split()))
# 비교대상을 위한 값
result = 0 

# list 접근을 위한 변수 생성
for i in range(num):
    for j in range(i+1, num):
        for k in range(j+1, num):
            # main_number보다 합이 클 경우 반복문 돌기
            if num_list[i] + num_list[j] + num_list[k] > main_number:
                continue
            # main_number보다 같거나 작을시 result값에 저장
            # 단, 이전 결과값보다 큰 경우에만 저장
            else:
                result = max(result, num_list[i] + num_list[j] + num_list[k])
print(result)