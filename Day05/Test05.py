#1. 1부터 100까지 정수를 출력하세요.
i = 1
while i <= 100:
    print(i)
    i += 1

#2. 1부터 100까지 정수중 짝수만 출력하세요. #반복문 안에 if
i = 1
while i <= 100:
    if i % 2 == 0:
        print(i)
    i += 1

#2. 1부터 100까지 정수중 홀수만 출력하세요. #반복문 안에 if
i = 1
while i <= 100:
    if i % 2 == 1:
        print(i)
    i += 1

print("="*10)
#4. 10부터 1까지 반복하여 6~3 꺼꾸로 출력
i = 10
while i >= 1:
    if 2 < i < 7:
        print(i)
    i -= 1
