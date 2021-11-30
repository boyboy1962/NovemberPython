# 구구단 게임
#1. 구구단 게임 5회 반복
#2. 정답을 맞추면 20점 추가
#3. 게임 종료후 성적을 출력
import random

score = 0
problem = 1
while problem <= 5:
    number1 = int(random.random()*8 + 2)
    number2 = int(random.random()*9 + 1)
    
    # print("{}번 문제\n  {} X {} = ?".format(problem, number1, number2))
    # answer = int(input("정답: "))
    answer = int (input("{} X {} = ".format(number1, number2)))
    
    if answer == number1 * number2 :
        score += 20
        print("정답")
    else:
        print("오답")
    
    problem += 1

print("점수: {}".format(score))
