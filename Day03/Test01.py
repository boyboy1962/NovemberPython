#IO - Input/Output - 입출력

#입력

#input()
# - 키보드에서 입력받는다.
# - 입력받는 값은 공간에 저장하여야한다.
# - input함수를 통하여 입력받은 데이터는 문자열로 반환돤다.
# - input함수를 통하여 입력받은 데이터는 내가 원하는 데이터롤 형변환을 해주어야한다.

#input만쓰면 문자열 형태로 입력받는다.
#공간 = input("출력하고자 하는 내용")

name = input("이름 이ㄺ : ")
print(type(name))
print(name)
age = input("나이입력 : ")
print(type(age))
print(age)
age = int(age)
print(type(age))

#1.input으로 입력받기(문자열)
#2.입력받은 값이 age변수에 저장 ( 문자열 str)
#3.age 변수공간 안에 있는 데이터를 형변환(str -> int)
#4.형변환한 데이터를 age 변수 공간에 다시 저장 (int 정수)

age = int(input("나이 입력: "))
print(type(age))
print("나이 : {}".format(age))
#1.input으로 입력받기 (문자열 str)
#2.입력받은 데이터를 형변환 (문자 str -> 정수 int)
#3.형변환한 데이터를 age 변수 공간에 저장 ( 정수 int )

hei = float(input("키 입력: "))
print(type(age))
print("키 : {}".format(hei))

# 정수 두개
a, b = int(input("정수 입력: " )), int(input("정수입력 :"))
print(a,b)

a = int(input("정수 입력: "))
b = int(input("정수 입력: "))
print(a,b)


