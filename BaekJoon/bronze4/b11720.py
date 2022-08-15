import sys

N=int(sys.stdin.readline())
num_list=list(int(sys.stdin.readline()))
result=0

for i in num_list:
    result += int(i)
print(result)