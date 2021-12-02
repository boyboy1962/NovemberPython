for i in "abcde":
    print(i)
print("----------------")
string = "abcde"
for i in range(0,5,1): #초기값, 끝값, 증감값 - 0~4 for i in range(5):
    print(string[i])
#0부터 시작하면 초기값(시작값)을 적어주지 않아도 된다.(기본값)
#종료값 보다 1 작을때까지 반복된다. (미만)
#1씩 증가될때는 증감값을 적지 않아도 된다.(기본값)
i = 0#초기값
while i < 5:#끝값
    print (string[i])
    i += 1 #증감값

    
print("========================")
for i in range(1,5):#초기값 : 1 끝값 : 5 (미만) 증감값 : 1 (생략가능)
    print(i)
#While
i = 1
while i < 5:
    print(i)
    i += 1
    

print("========================")
for i in range(1,6,2):#초기값 :1 끝값은 : 6(미만) 증감값 : 2
    print(i)
#while
i = 1
while i < 6:
    print(i)
    i += 2



print("========================")
for i in range(5, -1, -1): #증감값이 -일때 끝값이 1클때까지 반복 (초과)
    print(i)
#while
i = 5
while i > -1:
    print(i)
    i -= 1
