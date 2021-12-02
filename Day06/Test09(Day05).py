# 업다운 게임을 구현하려 합니다.
# 컴퓨터게게 1부터 100 사이의 정답을 생성하도록 코드를 구현한 뒤
# 사용자가 숫자를 입력하여 정답을 맞추도록 프로그래밍하세요.

# <게임의 상태>
# [업] 사용자가 정답보가 낮은 값을 입력한 경우
# [다운] 사용자가 정답보다 높은 값을 입력한 경우
# [정답] 사용자가 정답과 같은 값을 입력한 경우, 게임 종료(종료 지점)

# 게임 종료시 총 입력한 횟수를 화면에 출력

# 사용자가 정답을 입력하기 전까지 무한 반복
import random

number = int(random.random()*100) + 1
count = 0

while True:
    count += 1
    userNumber = int(input("숫자를 맞춰 보세요: "))
    if userNumber < number:
        print("[업]")
    elif userNumber > number:
        print("[다운]")
    else:
        print("[정답]")
        print("총 입력 횟수 : {}".format(count))
        break
print("총 횟수: " + str(count))

#선생님 다른 풀이 내용 무한 반복이 아니라 조건 반복
user = 0
com = int(random.random() * 100) + 1
cnt = 0
while user != com: #user값과 com의 값이 똑같으면 False가 되므로 반복문종료
    user = int(input("숫자 입력:"))
    cnt += 1

    if user > com:
        print("[down]")
    elif user < com:
        print("[업]")
    else:
        print("[정답]")
        print("총 입력횟수 : {}".format(cnt))
        
