import math

vacation = int(input())
koreanbook = int(input())
mathbook = int(input())
korean_solve = int(input())
math_solve= int(input())

clear_korean = math.ceil(koreanbook/korean_solve)
clear_math = math.ceil(mathbook/math_solve)

print(vacation-max(clear_korean,clear_math))