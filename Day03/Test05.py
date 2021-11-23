# 문제1) 월급을 입력 받기 (단! 세금 10%제외)
#       나의 연봉을 출력!

month = int(input("월급을 입력하세요: "))
year  = month * 12 * 0.9
print("나의 연봉은 {}원".format(year))

# 문제2) 숫자2개 입력
#        서로 교환(교체) 출력!
#a,b = 10,20
#print(a,b)#20 10

a = input("숫자를 입력하세요: ")
b = input("숫자를 입력하세요: ")
print(a,b)
c = a
a = b
b = c
print(a,b)
a,b = b,a #python에서만 가능
print(a,b)

# 문제 3) 숫자 2개를 입력 받아, 합 출력

a = int(input("숫자를 입력하세요: "))
b = int(input("숫자를 입력하세요: "))
print(a + b)

# 문제 4) 숫자 1개를 일력받아, 홀수이면 True 출력

number = int(input("숫자를 입력하세요: "))
print(bool(number%2))
print(number%2 == 1)

# 문제 5) 성적을 입력 받아, 60점 이상이고 100점 이하이면 True 출력

number = int(input("성적을 입력하세요: "))
print(number >= 60 and number <= 100)
print(60 <= number <= 100) #python only
