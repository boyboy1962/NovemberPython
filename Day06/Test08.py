# 1 ~ 30까지 출력

#<출력 결과>
#1   2   3   4   5
#6   7   8   9   10
#11  12  13  14  15
#16  17  18  19  20
#21  22  23  24  25
#26  27  28  29  30

#외부 for문 세로줄 개수
#내부 for문 가로줄 개수

cnt = 0

rowNum = 8
colNum = 7

for i in range(rowNum):
    for j in range(colNum):
        cnt += 1
        print(cnt,end='\t')
    print()


for i in range(6): # 0~5 총 6번
    for j in range(5): # 0~4 총 30번
        cnt += 1
        print(cnt,end='\t')
    print()
