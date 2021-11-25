# - 점수를 3개 입력받아 평균이 60점 이상이고
#   각 점수가 40점 이상이면 합격, 아니면 불합격
# 국엉, 영어, 수학

#불합격 중 어떤 점수가 부족하여 불합격인지 출력
# ex) 국어 평균 미달

korean = int(input('국어점수를 입력하세요: '))
enlgish = int(input('영어점수를 입력하세요: '))
math = int(input('수학점수를 입력하세요: '))
average = (korean + enlgish + math) / 3

# print(average)

if korean >= 40 and enlgish >= 40 and math >= 40 and average >= 60:
    print('합격')
else:
    print('불합격')
    #불합격일때만 조건식을 확인 하면 되기 때문에...
    if(not korean >= 40):
        #print('국어 점수 미달 \t\t('+ str(40 - korean) + '점 부족)')
        print("국어",end=" ")
    if not enlgish >= 40:
        #print('영어 점수 미달 \t\t('+ str(40 - enlgish) + '점 부족)')
        print("영어",end=" ")
    if not math >= 40:
        #print('수학 점수 미달 \t\t('+ str(40 - math) + '점 부족)')
        print("수학",end=" ")
    if not average >= 60:
        #print('전체 평균 점수 미달 \t('+ str(60 - average) + '점 부족)')
        print("평균",end=" ")
    print("미달")

#점수 확인은 elif 쓰면
#end=" " 엔터를 없에고 띄어쓰기를 쓴다.
    
