#randint() randrange() 사용금지 
import random

# 1 ~ 100까지 랜덤 값을 출력하는 코드를 작성하시오.

print(int(random.random()*100) + 1)

# 100 ~ 999까지 랜덤 값을 출력하느 코드를 작성하시오.

print(int(random.random()*900) + 100)

# 'A' ~ 'Z'까지 임의의 문자 3자리를 출력하는 코드를 작성하시오.
print(chr(int(random.random()*26) + 65) + chr(int(random.random()*26) + 65) + chr(int(random.random()*26) + 65))
