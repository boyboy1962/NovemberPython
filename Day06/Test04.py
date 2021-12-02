# 1~100까지 누적 합을 구하는 코드를 작성하세요.
total = 0
for i in range(1, 101):
    total += i
print (total)

# 다음 문자열 변수에서 공백을 제외한 문자의 수를 구하세요.
st = "Python basic program language"

count = 0 
for i in st:
    if i == " ":
        print("공백 스킵")
    else:
        count += 1

print("공백을 제외한 문자의 수는 {}".format(count))

#for 문 range 사용
count = 0
for i in range(len(st)): #영번째 부터 시작하고 
    if st[i] == " ":
        print("공백 스킵")
    else:
        count += 1

print("공백을 제외한 문자의 수는 {}".format(count))


#for 문 range 사용 공백에서 값을 빼서 구하기
count = 0
for i in range(len(st)):
    if st[i] == " ":
        count += 1
print("공백을 제외한 문자의 수는 {}".format(len(st) - count))
        


# 선생님의 다른 풀이

cnt = st.__len__()
for i in range(0,len(st)):
    if st[i] == ' ':
        cnt -= 1
print(cnt)
