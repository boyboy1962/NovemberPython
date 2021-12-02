# 모든 제어문은 중첩이 가능하다...

# 다중 for문
# - for문안에 for문이 있는 형태
# - 중첩적인 구조를 가지는 for문

for i in range(1,4):# 외부 for 문 #외부 for문이 한번돌때
    print("{}번째 외부 for문 실행".format(i))
    for j in range(1, 4): #내부 for문 #내부for문은 초기값부터 끝값까지 반복이돈다.
        print("내부 forans 실행")
    print("{}번째 왜부for문 종료".format(i))
