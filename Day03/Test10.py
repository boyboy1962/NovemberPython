age = int(input("나이 입력 :"))
print((age>=20) and '성인' or '미성년자')

#형식
#if 조건식:
#   종속문장
#else :
#   종속문장

if age >= 20:
    print("성인")
else:
    print("미성년자")
    
if age < 20:
    print("미성년자")
else:
    print("성인")


# 짝수 홀수
if age % 2 == 0:
    print("짝수")
else:
    print("홀수")
    
if age % 2 == 0:
    print("짝수")
if age % 2 == 1:
    print("홀수")
    
