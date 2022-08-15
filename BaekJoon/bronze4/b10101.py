A= int(input())
B= int(input())
C= int(input())

result=A+B+C
if A==B==C == 60:
    print('Equilateral')
elif result == 180 and (A == B or B == C or A == C):
    print('Isosceles')
elif result == 180 and (A != B or B != C or A != C):
    print('Scalene')
else:
    print('Error')