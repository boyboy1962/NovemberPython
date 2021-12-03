ls = [  1,2,3,4 ]
print(ls)
print(type(ls))

a,b,c,d = ls#unpacking
print(a,b,c,d)
#packing 불가능 - tuple가능

ls[0] = 0#튜플은 값변경 x, 리스트는 값 변경 o
print(ls)

ls[1:3] = 6,7
print(ls)

for i in ls:
    print(i)

for i in range(len(ls)):
    print(ls[i])
