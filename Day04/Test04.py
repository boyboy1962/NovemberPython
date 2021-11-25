# - 수를 입력받아 짝수이면서 3의 배수이면 출력

# 짝수이면서 3의 배수입니다.
# 홀수이면서 3의 배수입니다.
# 짝수이면서 3의 배수가 아닙니다.
# 홀수이면서 3의 배수가 아닙니다.

number = int(input('숫자를 입력하세요: '))

# if elif

if (number % 2 == 0 and number % 3 == 0):
    print('짝수이면서 3의 배수입니다.')
elif (number % 2 == 1 and number % 3 == 0):
    print('홀수이면서 3의 배수입니다.')
elif (number % 2 == 0 and number % 3 != 0):
    print('짝수이면서 3의 배수가 아닙니다.')
elif (number % 2 == 1 and number % 3 != 0): # 해당문은 else 문으로 작성이 가능함
    print('홀수이면서 3의 배수가 아닙니다.')
#print('done')

# if안에 if
# 세상에 너무 비효율적인데... 

if number % 2 == 0:
    #print('짝수이면서',end=" ")
    if number % 3 == 0:
        #print('3의 배수입니다.')
        print('짝수이면서 3의 배수입니다.')
    else:
        #print('3의 배수가 아닙니다.')
        print('짝수이면서 3의 배수가 아닙니다.')
else:
    #print('홀수이면서',end=" ")
    if number % 3 == 0:
        #print('3의 배수입니다.')
        print('홀수이면서 3의 배수입니다.')
    else:
        #print('3의 배수가 아닙니다.')
        print('홀수이면서 3의 배수가 아닙니다.')

# 이건 어때?

if number % 2 == 0:
    print('짝수이면서',end=" ")
else:
    print('홀수이면서',end=" ")
if number % 3 == 0:
    print('3의 배수입니다.')
else:
    print('3의 배수가 아닙니다.')
