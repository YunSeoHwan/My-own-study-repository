import sys
input = sys.stdin.readline
n = int(input())
for i in range(n):
    # 문서 수, 찾으려는 위치
    doc_num, doc_index = map(int, input().split())

    # 중요도 list
    ip = list(map(int, input().split()))

    # 순서 변수
    order = 1

    while True:
        # 처음값이 최댓값일때
        if ip[0] == max(ip):
            # 처음값 index와 찾으려는 위치가 일치할때
            if doc_index == ip.index(max(ip)):
                print(order)
                break
            # 최댓값 지우고 순서증가, index감소
            else:
                ip.pop(0)
                order += 1
                doc_index -= 1
        # 처음값 맨 뒤로 이동
        else:
            a = ip.pop(0)
            ip.append(a)
            doc_index -= 1
        # index값이 음수라면 젤 마지막 위치 반환
        if doc_index < 0:
            doc_index += len(ip)