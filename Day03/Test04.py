# 학생이름 / 국어 / 영어 / 수학 점수를 입력 받아서 출력

#<입력 결과>
#학생이름 : 개똥이
#국어점수 : 80
#영어점수 : 80
#수학점수 : 80

# <출력 결과>
#======================= 학생 정보 ====================
#이름     국어      영어      수학      합계      평균
#개똥이    80       80       80        80       80.00

name = input("학생이름 : ")
korean = int(input("국어점수 : "))
english = int(input("영어점수 : "))
math = int(input("수학점수 : "))

addtion = korean + english + math
average = addtion/3

print("="*17," 학생 정보 " , "="*17)
print("이름 \t국어 \t영어 \t수학 \t합계 \t평균")
print("이름","국어","영어","수학","합계","평균", sep="\t")
print("{} \t{} \t{} \t{} \t{} \t{:.2f}".format(name,korean,english,math,addtion,average))

