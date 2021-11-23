# 1. input()으로 2개의 값을 받은 다음 더하기, 빼기, 곱하기, 나누기(실수), 나누기(몫), 나머지
# 연산을 하여 그결과를 출력하는 코드를 작성하시오
# 실수는 소수점 2번째다리까지만 출력
#10 + 20 = 30

a = int(input("정수 입력: "))
b = int(input("정수 입력: "))
print (str(a) + " +  " + str(b) + " = " + str(a + b))
print (str(a) + " -  " + str(b) + " = " + str(a - b))
print (str(a) + " *  " + str(b) + " = " + str(a * b))
print (str(a) + " /  " + str(b) + " = " + "{:.2f}".format(a / b))
print (str(a) + " // " + str(b) + " = " + str(a // b))
print (str(a) + " %  " + str(b) + " = " + str(a % b))

print("{} + {} = {}".format(a,b,a+b))
print("{} - {} = {}".format(a,b,a-b))
print("{} * {} = {}".format(a,b,a*b))
print("{} / {} = {:.2f}".format(a,b,a/b))
print("{} // {} = {}".format(a,b,a//b))
print("{} % {} = {}".format(a,b,a%b))
