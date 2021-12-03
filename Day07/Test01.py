tp = 1,2,3,4,5 #튜플: packing

for i in tp:
    print(i)

print(tp)
print(type(tp))

#인덱싱
print(tp[0])
print(tp[-5])

#슬라이싱
print(tp[1:3])

# tp[1] = 0 - tuple은 값 변경이 불가능하다.

tp = (1.234, 123, 'a', 'abc', (1,2), [1,2])
print(tp)
#가로    0 1 2      세로
tp = ( ( 1,2 ) ,    #0
       ( 1,2,3 ) ,  #1
       ( 1,2 ))     #2
print(tp)
print(tp[0])
print(tp[1])
print(tp[2])
#변수명[세로인덱스][가로인덱스]
print(tp[1][2])
print(tp[2][0])

#큰단위    0          1          2
tp = ( ( 1,2 ) , ( 1,2,3 ) , ( 1,2 ))     #2
#작은단위 0 1       0 1 2       0 1
#변수명[큰단위][작은단위]
print(tp[1][2])
print("-" * 10)
for i in tp:        #i = (1,2)  i = (1,2,3)     i = (1,2)
    for j in i:     #j = 1 , 2  j = 1 , 2 , 3    j = 1 , 2
        print(j)


tp = 1,2,3,4,5 #packing
a, b, c, d, e = tp
print(a, b, c, d, e)
