dd = { "Park" : {"age" : 25, "blood" : "B"} ,
       "Kim" : {"age" : 37, "blood" : "A"} }

print(dd["Park"])
print(dd["Park"]["age"])# dd[큰틀의 키값][작은틀의 키값]

for name in dd: #name = "Park" #name = "Kim"
    for key in dd[name]: #dd["Park"] -> key = "age" key = "blood"
                         #dd["Park"] -> key = "age" key = "blood"
        print(dd[name][key])

ld = [  {"name" : "Park" , "age" : 25 , "blood" : "B"},
        {"name" : "Kim" , "age" : 37 , "blood" : "A"} ]

#Park
print(ld[0]["name"])

#반복문 - 전체 key value값 출력

for num in range (len(ld)):
    for key in ld[num]:
        print(key , "-" , ld[num][key])

for i in ld:    # i = {"name" : "Park" , "age" : 25 , "blood" : "B"}
                # i = {"name" : "Kim" , "age" : 37 , "blood" : "A"}
    for key in i:
        print("{} : {}".format(key, i[key]))
