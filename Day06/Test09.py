# 문제 1)
"""
#
##
###
"""

for i in range(0,3):
    for j in range(i + 1): # j의 끝값: 1(미만) #ㅓ의 끝값 : 2(미만)
        print("#",end="")
    print()


#문제 2)
"""
###
##
#
"""

for i in range(0,3):
    for j in range(3 - i):
        print("#",end="")
    print()

#문제 3)
"""
@##
@@#
@@@
"""

for i in range(0,3):
    for j in range(i + 1):
        print("@",end="")
    for j in range(2 - i):
        print("#",end="") 
    print()


#문제 4)
"""
  #
 ###
#####
"""

for i in range(0,3):
    for j in range(2 - i):
        print(" ",end="")
    for j in range(i + 1):
        print("#",end="")
    for j in range(i):
        print("#",end="")
    print()
   
