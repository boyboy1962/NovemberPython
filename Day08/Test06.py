# 학생의 인적 사항 등록 후 검색 프로그램
# - 학번 , 이름 , 주소
# {학번 : { name : 이름 , addr : 주소 } }

#1. 인적사항 등록
#2. 검색 - 학번 검색
#3. 수정
#4. 삭제
#5. 전체 보기
#6. 종료

info = {}
#info = { 학번 : { 'name' : 이름, 'addr' : 주소} }

while True:
    print('''
1. 인적사항 등록
2. 검색 - 학번 검색
3. 수정
4. 삭제
5. 전체 보기
6. 종료''')
    select = int(input("번호 입력 : "))
    if select == 1:
        studentNum = int(input("학번 입력: "))
        if info.get(studentNum) == None:
            name = input("이름 입력: ")
            addr = input("주소 입력: ")
            info.update({ studentNum : { 'name' : name , 'addr' : addr}})
        else:
            print("해당 학번은 이미 존재 합니다")
        
    elif select == 2:
        studentNum = int(input("학번 입력: "))
        if info.get(studentNum) == None:
            print("해당 학번은 존재하지 않습니다.")
        else:
            print("학번: " + str(studentNum))
            print("이름: " + info[studentNum]['name'])
            print("주소: " + info[studentNum]['addr'])
            
    elif select == 3:
        studentNum = int(input("학번 입력: "))
        if info.get(studentNum) == None:
            print("해당 학번은 존재하지 않습니다.")
        else:
            name = input("변경 이름 입력: ")
            addr = input("변경 주소 입력: ")
            info[studentNum].update({ 'name' : name , 'addr' : addr })

    elif select == 4:
        studentNum = int(input("학번 입력: "))
        if info.get(studentNum) == None:
            print("해당 학번은 존재하지 않습니다.")
        else:
            name = input("이름 입력 : ")
            if info.get(studentNum)["name"] == name:
                info.pop(studentNum)
                print("{}님이 삭제되었습니다.".format(name))
            else:
                print("이름이 잘못되었습니다.")
            
    elif select == 5:
        for studentNum in info:
            print("학번: " + str(studentNum))
            print("이름: " + info[studentNum]['name'])
            print("주소: " + info[studentNum]['addr'])
            

    elif select == 6:
        break
    
    else:
        print("잘못 입력하였습니다.")
