#모듈
# - 어떠한 기능들이 정의되어 있는 곳
# - 파이썬에서 왠만한 기능들이 모두 정의되어있다.
#   기능을 사용하려면 모둘을 지정하여 불러와서 사용하면 된다.

# - 형식
# from 모듈명 import 함수명
#   - 모듈안에 있는 일부 기능을 사용하기 위한 방식
# import 모듈명
#   - 모듈 전체

#random 모듈 - 임의의 수를 구하는 함수들이 정의되어 있는 모듈
import random

#임의의 수 구하기

#random()
# - 0 ~ 1미만의 실수를 구하느 함수
# - 0.0000 ~ 0.9999

#내가 원하는 범위 안의 수를 구하기
#int(random.random() * 범위 안의 수의 개수) + 시작수
#20 ~ 24 #20 21 22 23 24 -> 5개 (범위 안의 수의 개수) 시작수 : 20
#int(random.random() * 5) + 20

a = random.random() #0.0000 ~ 0.9999
b = a * 5 # 0.0000 ~ 4.9999
c = int(b) # 0 ~ 4
d = c + 20 # 20 ~ 24
print(d)
rand = int(random.random() * 5) +20
print(rand)


#1 ~ 5
rand = int(random.random() * 5) + 1

#2 ~ 10
rand = int(random.random() * 9) + 2
