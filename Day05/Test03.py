# 다음 조건을 보고 회원가입을 위한 프로그램 코드를 작성하시오.
# 아이디는 반드시 10자리 이상
# 패스워드는 반드시 8 ~ 16자리 사이
# 패스워드에 아이디가 포함된면 안됨

ID = input("ID: ")
PW = input("PW: ")

if (len(ID) < 10): # user.__len__()
    print("아이디는 반드시 10자리 이상이여야만 합니다.")
    print("현재 아이디는 {}이고 {}자리입니다.".format(ID ))
elif(len(PW) < 8 or 17 < len(PW)):
    print("패스워드는 반드시 8 ~ 16자리로 입력해 주세요.")
elif(PW.find(ID) != -1):
    print("패스워드에 아이디가 포함된면 안됨니다.")
else:
    print("완료하였습니다.")

if ID.__len__() >= 10:
    PW = PW = input("PW: ")
    if PW.__len__() < 8 or PW.__len__() > 16:
        print("비밀번호는 8자에서 16자 사이여야합니다.")
    elif pw.find(ID) >= 0:
        print("비밀번호에 아이디를 포함시킬 수 없습니다.")
    else:
        print("아이디 : {}".format(ID))
        print("비밀번호 : {}".format(PW))
else:
    print("아이디는 바드시 10자리 이상이여야합니다.")
