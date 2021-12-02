# 1 ~ 30까지 출력

#<출력 결과>
#1   2   3   4   5
#6   7   8   9   10
#11  12  13  14  15
#16  17  18  19  20
#21  22  23  24  25
#26  27  28  29  30

numberOfRow = 7

for i in range(1, 31):
    if i % numberOfRow == 0:
        print(i)
    else:
        print(i,end="\t")

for i in range(1,31):
    print(i,end="\t")
    if i % 5 == 0:
        print()
