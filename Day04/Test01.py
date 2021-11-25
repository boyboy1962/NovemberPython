# 두 수를 입력받아서 큰수를 출력(단, 같은 수면은 같다라고 출력)

number1 = int(input('첫번째 숫자를 입력하세요: '))
number2 = int(input('두번째 숫자를 입력하세요: '))

# 위에 부터 실행을 하고 조건이 맞으면 아래의 조건식을 실행하지 않는다.
if number1 > number2 :
    print('첫번째 숫자 ' + str(number1) + '이 두번째 숫자' + str(number2) + '보다 큽니다.' )
elif number2 > number1 :
    print('두번째 숫자 ' + str(number2) + '이 첫번째 숫자' + str(number1) + '보다 큽니다.' )
else:
    print('양 숫자의 값이 동일합니다.')

# 하나 하나씩 모두 실행
if number1 > number2 :
    print(number1)
if number1 < number2 :
    print(number2)
if number1 == number2 :
    print('같다')
            
print('done')

#if는 모든 if문을 다 확인하지만 elif는 위 if문이 거짓일때만 순차적으로 실행한다. 
