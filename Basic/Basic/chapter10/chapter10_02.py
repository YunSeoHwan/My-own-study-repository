# Chapter10_2
# Hangman(행맨) 미니 게임 제작(2)
# 프로그램 완성 및 최종 테스트

from ctypes import windll
import time

# CSV 처리
import csv

# 랜덤
import random

# 사운드 처리
import winsound

# 처음 인사
name = input("What is your name? ")
print('Hi, ', name, 'Time to play hangman game!')

print()

time.sleep(1)       # 1초 쉬기

print('Start Loading...')
print()
time.sleep(0.5)

# CSV 단어 리스트
words= []

# 문제 CSV 파일 로드
with open('./Basic/chapter10/resource/word_list.csv', 'r') as f:
    reader = csv.reader(f)
    # Header skip
    next(reader)
    for c in reader:
        words.append(c)

# 리스트 섞기
random.shuffle(words)

q = random.choice(words)

# 정답 단어
word = q[0].strip()

# 추측 단어
guesses = ''

# 기회
turns = 10

# 핵심 While
while turns > 0:
    
    # 실패 횟수
    failed = 0

    # 정답 단어 반복
    for char in word:

        # 정답 단어 내에 추측 문자가 포함되어 있는 경우
        if char in guesses:
            # 추측 단어 출력
            print(char, end=' ')
        else:
            # 틀린 경우 _ 출력
            print('_', end=' ')
            failed += 1
        
    # 단어 추측이 성공한 경우
    if failed == 0:
        print()
        print()
        # 성공 사운드
        winsound.PlaySound('./Basic/chapter10/sound/good.wav', winsound.SND_FILENAME)
        print('Congratulations!!!')

        # while문 탈출
        break
    
    # 추측 단어 입력
    print()
    print('Hint : {}'.format(q[1].strip()))
    guess = input('guess a charater ')
    print()

    # 단어 더하기
    guesses += guess

    # 정답 단어에 추측한 문자가 포함 안되었을때
    if guess not in word:
        # 기회 감소
        turns -= 1
        # 오류 메시지
        print('Oops! Wrong')

        # 남은 기회 출력
        print('You have', turns, 'more guesses!')

        if turns == 0:
            # 실패 사운드
            winsound.PlaySound('./Basic/chapter10/sound/bad.wav', winsound.SND_FILENAME)
            # 실패 메시지
            print('You hangman game failed. Bye!')