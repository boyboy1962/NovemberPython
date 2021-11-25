# 중국집 주문 프로그램

# 사용자에게 자장면, 짬뽕 주문 수량을 입력받아 결재 금액을 계산하여 출력

# 자장면 - 5000원
# 짬뽕 - 6000원

# 5그릇 이상 주문하면 3천원 할인되도록 금액을 계산하여 출력해주세요.
# 10그릇 이상 주문하면 10 할인 처리
    

blackPrice = 5000
redPrice = 6000

blackAmount = 0
redAmount = 0

ea1 = 5
ea2 =10

rate1 = 3000
rate2 = 10

print("안녕하세요 주문을 입력해주세요.")
print("자장면\t5000원")
print("짬뽕\t6000원")
print("{}그릇 이상 주문하시면 {}원 할인".format(ea1, rate1))
print("{}그릇 이상 주문하시면 {}% 할인".format(ea2, rate2))
print(" ")

blackAmount = int(input("주문하실 자장면의 수:\t"))
redAmount = int(input("주문하실 짬뽕의 수:\t"))

totalAmount = blackAmount + redAmount
totalPrice = (blackAmount * blackPrice) + (redAmount * redPrice)

if totalAmount >= ea2:
    totalPrice = totalPrice/100*((100-rate2))
elif totalAmount >= ea1:
    totalPrice = totalPrice - rate1
print("총금액 : " + str(totalPrice) )
