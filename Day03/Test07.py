import random

#randint(m,n)
# - 지정한 범위 안의 임의의 수를 구하는 함수
# - m ~ n
rand = random.randint(0,4) # 0 ~ 4
print(rand)

rand = random.randint(2,10) # 2 ~ 10
print(rand)

#randrange(m,n,p)
# - 범위 안의 임의의 정수값을 구하는 함수
# - m ~ n 미만
# - p는 생략 가능.. p만큼 증가한 값들 중에
rand = random.randrange(1,2) # 1부터 2미만 -> 1
print(rand)

rand = random.randrange(2) # 0부터 2미만까지 : 0은 생략 가능
print(rand)

rand = random.randrange(1,10,2) # 1부터 2미만까지 2씩 중가한 값들 중에...
print(rand)#1 3 5 7 9
