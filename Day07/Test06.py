menu = [
        ['칼국수', 6000],
        ['비빔밥', 5500],
        ['되지국밥', 7000],
        ['돈까스', 7000],
        ['김밥', 2000],
        ['라면', 2500]
       ]

#위의 리스트 구조를 보고 아래에서 요구하느 결과가 반영 되도록 코드를 작성하시오

# 비빔밥과, 돈까스의 가격을 출력하시오.
print("{} : {}".format(menu[1][0], menu[1][1]))
print("{} : {}".format(menu[3][0], menu[3][1]))

# 사용자 입력으로 메뉴와 가격을 입력 받아 menu 변수에 자료를 추가하는 코드를 작성 하시오.
user = input("메뉴 입력: ")
price = int(input("가격 입력:"))
menu.append([user, price])

print(menu)
# 사용자 입력으로 메뉴와 가격을 입력 받아 menu 변수에 자료를 추가 할 때
# 기존에 동일한 메뉴가 존재하는 경우 가격만 변경되도록 코드를 작성하시오.
user = input("메뉴 입력: ")
noMenu = True
for ls in menu:
    if user == ls[0]:
        ls[1] = int(input("변경할 가격 입력: "))
        noMenu = False
        break
if noMenu:
    price = int(input("가격 입력:"))
    menu.append([user, price])

print(menu)
    
user = input("메뉴 입력: ")
noMenu = True
for num in range(len(menu)):
    if user == menu[num][0]:
        menu[num][1] = int(input("변경할 가격 입력: "))
        noMenu = False
        break
if noMenu:
    price = int(input("가격 입력:"))
    menu.append([user, price])

print(menu)

#메뉴를 자동으로 선택하여 출력하는 코드를 작성 하시오.
import random

number = int(random.random() * len(menu))
print("오늘의 메뉴는 {} 가격은 {}원입니다.".format(menu[number][0],menu[number][1]))
