a=[]
b=[]

x,y= map(int,input().split())

for row in range(x):
    row =list(map(int,input().split()))
    a.append(row)

for row in range(x):
    row =list(map(int,input().split()))
    b.append(row)

for row in range(y):
    for col in range(x):
        print(a[row][col]+b[row][col], end=' ')

    print()