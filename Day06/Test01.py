# [아이템 강화 시뮬레이션 ]
# 1. 아이템은 1번 강화하는데 현금 1000원이 필요하다
# 2. 아이템은 처음에 레벨이 0이다.
# 3. 강화가 성공할 확률은 35%이고 성공하면 레벨이 1증가
# 4. 강화가 실패할 확률은 30%이고 실패하면 레벨이 1감소
# 5. 그 외의 경우에는 아무런 변화가 없다.

# 0 레벨의 아이템을 10 레벨로 만들기 위해 내가 쏟아 부어야 되는
# 현금을 계산하세요.

import random

itemLevel = 1 
success = 35
fail = 30
tryCost = 1000
count = 0

while True:
    count += 1
    enhance = int(random.random() * 100) + 1
    if enhance <= success:
        print("강화에 성공하셨습니다.")
        itemLevel += 1
        print("아이템 레벨 :" + str(itemLevel))
    elif enhance >= 100 - fail:
        print("강화에 실패하였습니다.")
        itemLevel -= 1
        if itemLevel == 0:
            itemLevel = 1
            print("아이템의 레벨이 1보다 낮아 질 수 없습니다.")
        else:
            print("아이템 레벨 :" + str(itemLevel))
    else:
        print("변화가 없습니다.")
        print("아이템 레벨 :" + str(itemLevel))

    if itemLevel == 10:
        print("지불한 가격: " + str(tryCost * count))
        break

tot = 0
lev = 0

while True:
    rate = int(random.random() * 100) + 1
    tot += 1000

    if(rate <= 35):
        lev += 1
        print("강화 성공!!+{}".format(lev))
        if lev == 10:
            print("강화 종료\n 총 금액 : {}원".format(tot))
            break
    elif rate >= 70:
        if lev == 0:
            print("강화실패!! 0및으로는 하락할 수 없습니다+{}".format(lev))
        else:
            lev -= 1
            print("강화 실패!!+{}".format(lev))
    else:
        print("아무런 변화가 없습니다.")


tot = 0
lev = 0
while lev < 10:
    rate = random.random() #0.0000~0.9999
    tot += 1000

    if rate < 0.35:
        lev += 1
        print("강화 성공+{}".format(lev))
    elif rate >= 0.7:
        if lev == 0:
            print("강화 실패!! 0밑으로 하락할 수 없습니다+{}".format(lev))
            continue #else 대용으로 사용하고 밑에 있는 모든 코드들을 실행하지 않고 다시 반복문 처음으로 돌아간다.
        lev -= 1
        print("강화실패!!+{}".format(lev))
    else:
        print("아무런 변화가 없습니다 + {}".format(lev))
print("강화 종료\n 총 금액 : {}원".format(tot)) 
