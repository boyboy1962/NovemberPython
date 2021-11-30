# 문자열에서 사용하는 함수

msg = "              abcdefghijklmnopqraaa       "

# find(str)
# - 문자열에서 특정 문자열을 찾아 해당하는 문자의 인덱스 값을 반환하는 함수
# - 없으면 -1을 반환, 있으면 인덱스 값을 반환
print(msg.find("f"))
print(msg.find("z"))
print(msg.find(""))


#count(str)
# - 문자열에서 특정 문자열을 찾아서 해당 문자열의 수를 반환하는 함수
print(msg.count("a"))


#lower() - 대문자를 소문자로 변환
#upper() - 소문자를 대문자로 변환
#swapcase() - 소문자는 대문자, 대문자는 소문자로 변환
s = "AbCdEf"
print(s)
print(s.lower())
print(s.upper())
print(s.swapcase())


#islower() - 문자열이 소문자면 True, 소문자 이외에 다른게 있으면 Flase
print(s.islower())
# - s를 소문자로 만든다음에 islower을 사용하여 True를 뜨게 만드세요.
# 1 
print(s.islower())
# 2
s_lower= s.lower()
print(s_lower.islower())
# 둘다 풀이 내용으로 나왔다.


# isupper() - 문자열이 대문자면 True, 대문자 이외에 다른게 있으면 False
print(s.isupper())
print(s.upper().isupper())


# - 공백 제거 함수
# strip - 앞 뒤 제거
# lstrip - 좌측 제거
# rstrip - 우측 제거
print("|{}|".format(msg))
print("|{}|".format(msg.strip()))
print("|{}|".format(msg.lstrip()))
print("|{}|".format(msg.rstrip()))


#replace(old,new)
# - old문자열을 new문자열로 치환하는 함수
print(msg.replace("ab","가나").strip())#치환 후 공백제거
print(msg.strip().replace("ab","가나"))#공백제거 후 지환


#split(str) ***
# - 문자열을 특정 문자열로 분리하는 함수.
# - 분리하면 인데싱 되어 있다.
msg = "빨-주-노/초-파/남-보"
print(msg.split("-"))# - 이부분으로 분리된다.
print(msg.split("/"))# / 이부분으로 분리된다.

ls = msg.split("-")
print(ls)
print(ls[2].split("/"))

msg = "홍길동/20-이몽룡/30"
personList = msg.split("-") 
print(personList)
print(personList[0].split("/"))
print(personList[1].split("/"))

for person in personList:
     print(person.split("/"))
    


