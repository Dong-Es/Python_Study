timea, timeb, timec = map(int,input().split())

plustime =int(input())

remainderc=(timec+plustime)&60
c=(timec+plustime)//60

timeb=timeb+c
remainderb=timeb%60
if timeb >60:
    b=timeb//60

timea=timea+b

if timea > 24:
    a=timea