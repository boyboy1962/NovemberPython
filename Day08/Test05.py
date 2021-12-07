# 가수이름, 구성원 수 입력받고 출력까지 할 수 있는 코딩
#(5명만 입력하고 출력하세요)
#단, 가수이름 겹치기 않게

dic = {}
keys = list(dic.keys())

while len(dic) < 5 :
    keys = list(dic.keys())
    name = input("가수이름: ")
    number = int(input("구성원 : "))
    
    if dic.get(name) == None:
        dic.update({name : number})
    else:
        print("데이터가 이미 존재합니다.")

for key in dic:
    print("{} : {}".format(key,dic[key]))
