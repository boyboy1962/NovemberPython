# 1부터 100까지의 정수
for i in range(1, 101):
    print(i, end=" ")
print()

# 53부터 25까지의 정수
for i in range(53, 24, -1):
    print(i, end=" ")
print()

# 30부터 60까지의 홀수
for i in range(31, 61, 2):
    print(i, end=" ")
print()

for i in range(30, 61, 1): #증감식 스킵 가능
    if (i % 2 == 1):
        print(i, end=" ")
print()

# 100 부터 0까지의 5의 배수
for i in range(100, -1, -5):
    print(i, end=" ")
print()

for i in range(100, -1, -1):
    if i % 5 == 0:
        print(i, end=" ")
print()

# A부터 Z까지의 알파벳
for i in range(ord("A"), ord("Z") + 1, 1):
    print(chr(i), end=" ")
print()
               
# 숫자 1개를 입력받아 1부터 해당 수 까지 출력
number = int(input("수를 입력: "))
for i in range(1, number + 1): # 해당 수까지라서 1을 더해 줘야한다.
    print(i, end=" ")
print()
    
# 숫자 1개를 입력받아 1부터 해당 수 까지 홀수 출력
number = int(input("수를 입력: "))
for i in range(1, number + 1):
    if i % 2 == 1 :
        print(i, end=" ")
print()
