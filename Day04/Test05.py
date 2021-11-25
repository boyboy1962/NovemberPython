# 이름, 학번, 3과목의 성적을 입력받아 합계와 평균을 구하고,
# 평균이 90이상이면 'A', 80 이상 'B' 70이상 'c', 60이상 'D', 60미만 이면 'F'를 출력하시오

# 이름은 {}이고 학번은 {}이며 학점은 {}입니다.

name = input("학생이름 : ")
studentNumber = input("학번\t: ")# 학번을 숫자로 받아라 
korean = int(input("국어점수 : "))
english = int(input("영어점수 : "))
math = int(input("수학점수 : "))

total = korean + english + math
average = total/3

grade = "" 

print('이름은 {}이고 학번은 {}이며 학점은'.format(name,studentNumber),end=" ")

#elif는 위 조건식이 거짓일때만 순차적으로 실행되기 때문에 90미나의 조건이 포함되어있다.
if average >= 90:
    print("A",end="")
    grade ="A"
elif average >= 80:
    print("B",end="")
    grade ="B"
elif average >= 70:
    print("C",end="")
    grade ="C"
elif average >= 60:
    print("D",end="")
    grade ="D"
else:
    print("F",end="")
    grade ="F"

print('입니다')

#이건 선생님 풀이 깔끔하다...
print('이름은 {}이고 학번은 {}이며 학점은 {}입니다.'.format(name,studentNumber,grade))

# if문에 python 비교 방식 쓰기 비효율적이니 쓰지 말것
if average >= 90:
    print("A",end="")
if 90 > average >= 80:
    print("B",end="")
if 80 > average >= 70:
    print("C",end="")
if 70 > average >= 60:
    print("D",end="")
if 60 > average:
    print("F",end="")
