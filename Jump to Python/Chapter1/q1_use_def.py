def avg():
    korean, english, math = map(int,input('국어 영어 수학 순으로 점수를 입력하시오. : ').split())
    result= (korean+english+math)//3

    return result

print(avg())

