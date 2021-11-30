# 어떤 수의 약수를 구하는 프로그램을 작성
# 약수 어떤수를 정수로 나눌 수 있는 수
# ex) 8 #입력
# 출력 : 1 2 4 8

number = int(input("숫자 입력: "))
i = 1

while i <= number:

    if number % i == 0:
        print(i, end=" ")

    i += 1
