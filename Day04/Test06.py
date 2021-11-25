# 영문자를 입력 받아 대,소문자를 구분 한 뒤 소문자는 대문자로 재문자는 소문자로 서로 변환하여 출력하시오
# - > 특수문자 및 숫자를 입력할 시 잘못된 입력이라는 문구 표시

#입력 : A
#A의 소문자 : a

#입력 : a
#a의 대문자 :A

letter = input("알파벳를 입력해주세요: ")
asciiNum = ord(letter)

if 65 <= asciiNum <= 90 :
    print("입력 : " + letter)
    print(letter + "의 소문자 : " + chr(asciiNum + 32))
    print("입력 : {} \n{}의 소문자 : {}".format(letter,letter,chr(asciiNum + 32)))
elif 97 <= asciiNum <= 122 :
    print("입력 : " + letter)
    print(letter + "의 대문자 : " + chr(asciiNum - 32))
    print("입력 : {} \n{}의 대문자 : {}".format(letter,letter,chr(asciiNum - 32)))
else :
    print(letter + "는 알파벳이 아닙니다.")

print("\n아래는 선생님 풀이")
# 인식을 할때 그냥 단어를 숫자로 인식하기 그냥 써도 무방하다.
if 'A' <= letter <='Z':
    print("{}의 소문자 : {}".format(letter,chr(asciiNum + 32)))
if 'a' <= letter <='z':
    print("{}의 대문자 : {}".format(letter,chr(asciiNum - 32)))
else :
    print("잘못된 입력입니다..")
