# 빙고판 채우기.......
# 1 ~ 25 중복없이 5 * 5 채워져야 한다....

import random

ls = [[0,0,0,0,0],
      [0,0,0,0,0],
      [0,0,0,0,0],
      [0,0,0,0,0],
      [0,0,0,0,0]]

#랜덤 인덱스 2개
#i의 값이 1~25
#for x while o

number = 1
while number <= 25:
    row = int(random.random() * 5)
    col = int(random.random() * 5)

    if ls[row][col] == 0:
        ls[row][col] = number
        number += 1
    for item in ls:
        print(item)
    print("===================")
