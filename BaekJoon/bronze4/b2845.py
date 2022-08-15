height,width=map(int,input().split())

people=list(map(int,input().split()))

party = width*height

for i in people:
    print(i-party,end=' ')