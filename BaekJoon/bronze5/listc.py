a=[]
b=[]
# a list b list 생성한거에여 (여기에는 아무것도 들어있지 않아요)
x,y = map(int,input().split())
#n,m크기의 행렬 이라고 했는데 x(행 가로),y(열 세로)
for row in range(x):
  row=list(map(int,input().split()))
  # a x행만큼 값을 넣어준다.
  a.append(row)
  # a list에 row값을 cheom-boo한다.

for row in range(x):
  row=list(map(int,input().split()))
  # b x행만큼 값을 넣어준다.
  b.append(row)
  # b list에 row값을 cheom-boo한다.

for row in range(x):
  for col in range(y):
    print(a[row][col]+b[row][col],end=' ')

