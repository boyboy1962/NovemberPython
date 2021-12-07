dic = { "숫자" : 0 , "실수" : 1.1 , "과일" : ["포도","딸기"]}

print(dic)
print(type(dic))
print(dic["숫자"])
print(dic["실수"])
print(dic["과일"])
print(dic["과일"][0])
print(dic["과일"][1])

for key in dic: #dic의 키값만 key변수에 담긴다.
    #key = "숫자" #key = "실수" #key = "과일" 
    print(key, "-", dic[key])
