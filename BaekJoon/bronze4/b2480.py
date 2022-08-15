one, two, three = map(int,input().split())

if one== two == three:
    print(10000+1000*one)
elif one == two or one == three:
    print(1000+100*one)
elif two== three:
    print(1000+100*two)
else:
    print(max(one,two,three)*100)
