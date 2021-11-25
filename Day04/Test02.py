# - 수를 입력받아 0보다 크고 100보다 작으면 정상
#   아니면은 비정상 출력

number = int(input('숫자를 입력하세요: '))

#python 값비교
if (0 < number < 100):
    print('정상')
else:
    print('비정상')

#and or - 논리연산자 
if (number > 0 and number < 100):
    print('정상')
else:
    print('비정상')
    
# 어떤 것이 효율적일까
# 그리고 괄호좀 쓰지말자...
# 아래는 장난친것

if (number > 0):
    if (number < 100):
        print('정상')
    else:
        print('비정상')
else:
    print('비정상')
