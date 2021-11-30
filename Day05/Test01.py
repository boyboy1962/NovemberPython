# 문자열
# - 모든 프로그래밍 언어에서는 문장을 문자열이라고 부른다.
# - 문자가 여러개 모여서 저장되는 형채
# - 메모리에 저장될때 연속적인 공간들이 만들어지고 하나의 공간에 하나의 문자가 저장되는 형태
print("abcd")
string = "abcd"
print(string)

# (string[0])   (string[1])     (string[2])     (string[3]) 
# (string[-4])  (string[-3])    (string[-2])    (string[-1])
# 여러개의 데이터를을 저장하는 공간 같은 경우 각각의 공간을 구분하기 위해서 인덱스라는 번호흫 붙여놓았다.
# 인덱스는 항상 0부터 시작하고 가장 마지막 요소는 공간의 개수보다 1작다.



#인덱싱
# - 인덱스 값을 총하여 특정 위치의 데이터를 출력하는 방식
# - []안에 인데스 값을 적어주면된다.
# - 인데스 범위를 벗어나게 되면 error
print(string[0])
print(string[1])
# print(string[4]) -인덱스 번위가 벗어나기때문에 error
print(string[-1])
print(string[-4])



#__len__() - 데이터의 공간의 개수를 구하는 함수
print(string.__len__())
#len(연속적인 공간) - 데이터의 공간의 개수를 구하는 함수
print(len(string))



#슬라이싱
# - 인덱싱을 이용하여 부분적으로 잘라내는 것..
# - [m:n] - m부더 n이전(미만)
print(string[1:3])
print(string[1:])#1번째 인데스 부터 ~
print(string[:2])#처음부터 2번째 인덱스 전까지

a = string[1:3]
print(a)
b = string[0]
print(b)
