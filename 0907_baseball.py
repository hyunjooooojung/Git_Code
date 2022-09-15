import random
import time
from datetime import datetime



#랜덤으로 생성된 숫자들을 com_rand에 배열 형태로 입력해준다. 이건 컴퓨터가 랜덤으로 정하는 숫자들
def make_number():
    com_rand = list(random.sample(range(10), n))
    print(f"0과 9 사이의 서로 다른 숫자 {n}개를 랜덤하게 뽑았습니다.")
    return com_rand


def user_rand():   #사용자가 랜덤으로 숫자를 입력하는 함수
    print(f"숫자 {n}개를 하나씩 입력하세요!")

    guess_list = []
    while len(guess_list) < n:
        guess = int(input(f"{len(guess_list)+1}번째 숫자를 입력하세요: "))

        #예외 조건 설정 if & elif/ else는 옳은 조건
        if guess < 0 or guess > 9:
            print("범위를 벗어나는 숫자입니다. 다시 입력해주세요 :)")
        elif guess in guess_list:
            print("중복된 숫자를 입력하셨습니다. 다시 입력해주세요 :)")
        else:
            guess_list.append(guess)

    return guess_list


def get_score(guess, answer, out):
    strike_count = 0
    ball_count = 0
    out_count = 0

    for i in range(n):
        if guess[i] == answer[i]:
            strike_count += 1   #뽑은 숫자와 일치하는 경우
        elif guess[i] in answer and guess[i] != answer[i]:
            ball_count += 1     #일치하지 않는 경우
        elif guess[i] not in answer and guess[i] != answer[i]:
            out_count += 1
    
    return f"{strike_count} STRIKE", f"{ball_count} BALL", f"{out_count} OUT"





#게임 실행
start_time = time.time() # 프로그램이 시작된 현재 시간 저장
n = int(input()) #게임을 몇자리 숫자로 할 것인지 입력 0~9
ANSWER = make_number()   #컴퓨터가 만든 정답 랜덤 숫자들
OUT = 0      #숫자가 일치하지 않을 때 카운트 되는 변수
try_count = 0 #입력을 받을 때마다 1씩 증가

strike = 0 
ball = 0
out = 0

while True:
    GUESS = user_rand()
    strike, ball, out = get_score(GUESS, ANSWER, OUT)

    print(strike, ball, out)
    try_count += 1

    if strike == f"{n} STRIKE":   #all STRIKE 인 경우 게임종료 & break
        break
    elif n == "exit":
        break


print(f"축하합니다!! {try_count}번 만에 숫자 {n}개의 값과 위치를 모두 맞추셨습니다.")

#프로그램 실행시간, 종료시각 출력
end_time = time.time()  #프로그램이 종료된 현재 시간 저장
print(f"게임 실행 시간 : {end_time - start_time:.3f}초")
print(f"현재 시간 : {datetime.now()}")
print(f"도전 횟수 : {try_count}")
