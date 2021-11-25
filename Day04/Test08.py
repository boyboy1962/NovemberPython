# 주사위를 2개 던지는 코드를 구현하시고
# 두개의 주사위 합계에 따라 아래와 같이 코드를 구현

# (1) 합계가 짝수일 경우        짝! 출력
# (2) 합계가 홀수일 경우        홀! 출력
# (3) 두 주사위가 같은 값일 경우 더블! 출력

# 주사위 더블이 상위 계체라서 더블이 경우 무족건 더블 출력

import random

die1 = int(random.random()*6) + 1
die2 = int(random.random()*6) + 1
total = die1 + die2

print (die1, die2)

if (die1 == die2):
    print("더블! {}칸 앞으로 가고 한번 더 던지세요.".format(die1+die2))
elif (total % 2 == 0):
    print ("짝! {}칸 앞으로 가세요.".format(die1+die2))
elif (total % 2 == 1): # else 마무리 해도 무관함
    print ("홀! {}칸 앞으로 가세요.".format(die1+die2))


# 선생님 다른 풀이
if total % 2 == 0 and die1 != die2:
    print("짝!")
elif (total % 2 == 1):
    print("홀!")
else:
    print("더블!")
