dic = {"a" : 1 , "b" : 2 , "c" : 3}

#Dictionary(사전형)에서 사용되는 함수
#update(dic)
# - 사전형자료에 값을 추가한다.\
# - key값이 같으면 valeu값만 updata하고.. key값이 없으면 추가
dic.update({"a" : 4, "d" : 5})
print(dic)

#fromkeys(iter,value)
# - 리스트, 튜플에 존재하느 값을 키로 사전형 자료를 생성하여 반환한다.
# - value값은 일괄적으로 설정 될 수 밖에 없다.
ls = [ 1,2,3,4 ]
print(dic.fromkeys(ls,1))

#get(key, [value])
# - 사전형의 키를 통하여 값을 반환
# - 키값이 없으면 None을 반환
# - 키값이 있으면 value 값을 반환
# - 키값이 없어도 value 값을 설정하면 value값 반환
print(dic.get("a"))
print(dic.get("e"))
print(dic.get("e",1))

#keys()
# - 사전형의 모든 키를 반환한다.
# - 리스트나 튜플타입으로 변환하여 사용이 가능하다.
key = dic.keys()
print(key)

key = list(key)
print(key)

for i in key:
    print(i)

#values()
# - 사전형의 모든 값을 반환다.
# - 리스트와 튜플타입으로 변환하여 사용 가능하다.
# - 사전형의 모토가 벗어나므로 잘 사용되지 않는다.
print(dic.values())

#items()
# - 사전형의 모든 key - value를 쌍으로 튜플로 반환
# - 리스트나 튜플타입으로 변환하여 사용 가능
tp = dic.items()
print(tp)

#pop(key)
# - 사전형의 키를 통해 value값을 반환 후 삭제
# - key값이 없으면 error
print(dic.pop("a"))
print(dic)

#popitem()
# - 사전형의 key - value의 쌍을 튜플로 반환 후 삭제
# - 제일 끝에 있는 데이터부터 삭제
print(dic.popitem())
print(dic)

#clear()
# - 사전형의 모든 key - value를 삭제하여 빈 사전형 자료만 남는다.
dic.clear()
print(dic)
