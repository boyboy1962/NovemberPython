# 다음의 메뉴와 가격을 key와 value로 사용하여 사전형 자료를 만드시오. (변수명 : menu)
# 칼국수(6000원), 비빔밥(5500원), 돼지국밥(7000원),
# 돈까스(7000원), 김밥(2000원), 라면(2500원)
menu = { "칼국수" : 6000,
         "비빔밥" : 5500,
         "돼지국밥" : 7000,
         "돈까스" : 7000,
         "김밥" : 2000,
         "라면" : 2500}

#위에서 만든 사전형 자료 menu 변수에서 가격이 6000원 미만에 해당되는 메뉴와 가격을 출력하는 코드를 작성하시오.
for item in menu:
    if menu[item] < 6000:
        print ("{} - {}".format(item, menu[item]))

#사용자 입력으로 메뉴와 가격을 입력 받아 menu 변수에 자료를 추가 할 수 있도록 하시오. (동일한 메뉴는 가격만 변경)
newItem = input("메뉴 입력: ")
newPrice = int(input("가격 입력: "))

menu.update({newItem : newPrice})

print(menu)

#메뉴를 자동으로 선택하여 출력하는 코드를 작성하시오
# 실패함
import random
keys = list(menu.keys())
print(keys)
number = int(random.random() * len(keys))
print("{} : {}원".format(keys[number] , menu[keys[number]]))
