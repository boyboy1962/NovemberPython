number = int(input("아래 문제에 사용될 만한 숫자를 입력하시오: "))

#문제 1) 양수 , 0 , 음수 출력
if number > 0:
    print("양수")
elif number < 0:
    print("음수")
else:
    print("0")

#문제 2) 4의 배수 출력

if number % 4 == 0:
    print("4의 배수입니다.")
else:
    print("4의 배수가 아닙니다.")

#문제 3) 60점이상 합격, 불합격 출력
if number >= 60:
    print("합격")
else:
    print("불합격")
