ls = [ 1,2,3,4 ]
print(ls)

#ls[4] = 5 인덱스가 없기 때문에 error
ls.append(5) #맨뒤에 데이터 추가
print(ls)

ls.append((6,7)) #append는 데이터의 집합 모양 그대로 list에 추가시킨다.
print(ls)

ls. extend((6,7)) #extend는 데이터의 집하을 데이터 하나로 쪼개서 list에 추가

ls.insert(0,0) #insert(idx,값)
print(ls)

print(ls.pop())#pop() - 가장 뒤에 있는 데이터 삭제
print(ls)

print(ls.pop(6))#pop(idx) - 인덱스 안에 있는 데이터를 삭제
print(ls)

ls.remove(4) # 값으로 데이 터 삭제
print(ls)

ls.clear()# 초기화
print(ls)

ls = [4,7,1,4,7,2,8,3,7,4,2,4,8,0,9]
ls.reverse()
print(ls)

ls.sort()#오름차순
print(ls)

ls.sort(reverse = True)#내림차순
print(ls)
