numberOfLines = int(input("라인의 수를 정해주세요: "))

# 문제 1)
"""
#
##
###
"""
print("=" * numberOfLines)
for i in range(0,numberOfLines):
    for j in range(i + 1): # j의 끝값: 1(미만) #ㅓ의 끝값 : 2(미만)
        print("#",end="")
    print()
print("=" * numberOfLines)

#문제 2)
"""
###
##
#
"""
print("=" * numberOfLines)
for i in range(0,numberOfLines):
    for j in range(numberOfLines - i):
        print("#",end="")
    print()
print("=" * numberOfLines)

#문제 3)
"""
@##
@@#
@@@
"""
print("=" * numberOfLines)
for i in range(0,numberOfLines):
    for j in range(i + 1):
        print("@",end="")
    for j in range((numberOfLines - 1) - i):
        print("#",end="") 
    print()
print("=" * numberOfLines)


#문제 4)
"""
  #
 ###
#####
"""
print("=" * (numberOfLines * 2 - 1 ))
for i in range(0,numberOfLines):
    for j in range((numberOfLines - 1) - i):
        print(" ",end="")
    for j in range(i + 1):
        print("#",end="")
    for j in range(i):
        print("#",end="")
    print()
   
