snack, number, money = map(int,input().split())

result = snack*number

need_money= result-money

if need_money > 0:
    print(need_money)
else:
    print(0)