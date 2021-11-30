# 문제1) 1~5까지의 합 출력
# 정답1) 15
result = 0
i = 1
while i <= 5:
    result = result + i
    i += 1
print(result)

# 다른 방식
result = 0
i = 1
while True:
    result = result + i
    if i == 5:
        break
    i += 1
print(result)


# 문제2) 1~10까지 반복해 3미만 7이상만 출력
# 정답2) 1, 2, 4, 6, 9, 10
i = 1
while i <= 10:
    if i < 3 or i >= 7:
        print(i, end=", ")
    i += 1
print()

# 다른 방식
i = 1
while True:
    if i < 3 or i >= 7:
        print(i, end=", ")
    if i == 10:
        break
    i += 1
print()

# 문제3) 문제2의 조건에 맞는 수들의 합 출력
# 정받3) 37
result = 0
i = 1
while i <= 10:
    if i < 3 or i >= 7:
        result = result + i
    i += 1
print(result)

# 다른 방식
result = 0
i = 1
while True :
    if i < 3 or i >= 7:
        result = result + i
    if i == 10:
        break
    i += 1
print(result)


# 문제4) 문제2의 조건에 맞는 수들의 개수 출력
# 정답4) 6
result = 0
i = 1
while i <= 10:
    if i < 3 or i >= 7:
        result = result + 1
    i += 1
print(result)

# 다른 방식
result = 0
i = 1
while True:
    if i < 3 or i >= 7:
        result = result + 1
    if i == 10:
        break
    i += 1
print(result)
