menu = (
        ('칼국수', 6000),
        ('비빔밥', 5500),
        ('되지국밥', 7000),
        ('돈까스', 7000),
        ('김밥', 2000),
        ('라면', 2500)
       )
# 위의 튜플 구조를 보고 아래의 요구하느 값을 출렭하는 코드를 작성 하시오.

# 김밥과, 라면의 가격을 각각 출력하시오.

print("="*10 + "1번문제" + "="*10)
for ls in menu:
    if ls[0] == '김밥':
        print("김밥의 가격은 " + str(ls[1]))
    if ls[0] == '라면':
        print("라면의 가격은 " + str(ls[1]))
for num in range(len(menu)):
    if menu[num][0] == '김밥':
        print("김밥의 가격은 " + str(ls[1]))
    if menu[num][0] == '라면':
        print("라면의 가격은 " + str(ls[1]))

# 풀이 정답
print("{} : {}원".format(menu[4][0],  menu[4][1]))
print("{} : {}원".format(menu[5][0],  menu[5][1]))

# 가격이 7000에 해당하는 메뉴를 출력 하시오.

print("="*10 + "2번문제" + "="*10)
for ls in menu:
    if ls[1] == 7000:
        print(ls[0],end=", ")
print()
for num in range(len(menu)):
    if menu[num][1] == 7000:
        print(menu[num][0],end=", ")
print()

# 가격이 6000원 이하인 메뉴를 출력 하시오.

print("="*10 + "3번문제" + "="*10)
for ls in menu:
    if ls[1] <= 6000:
        print(ls[0],end=", ")
print()
for num in range(len(menu)):
    if menu[num][1] <= 6000:
        print(menu[num][0],end=", ")
print()

#사용자 입력으로 메뉴를 입력받아 해당하는 메뉴의 가격을 출력하시오.

print("="*10 + "4번문제" + "="*10)
user = input("메뉴 선택: ")

isItThere = True
for ls in menu:
    if (user == ls[0]):
        print("{}의 가격은 {}원입니다.".format(user, ls[1]))
        isItThere = False
        break
if (isItThere):
    print(user + "는 없습니다.")
    
isItThere = True
for num in range(len(menu)):
    if (user == menu[num][0]):
        print("{}의 가격은 {}원입니다.".format(user, menu[num][1]))
        isItThere = False
        break
if (isItThere):
    print(user + "는 없습니다.")

