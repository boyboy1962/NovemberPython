# 1 ~ 45까지 임의의 값을 중복 없이 6개 생성 하여 출력 하는 코드를 작성 하시오.
import random

ls = []

while len(ls) < 6:
    number = int(random.random() * 45) + 1

    if ls.count(number) == 0:
        ls.append(number)
    #print(str(ls) + str(number))
print(ls)
