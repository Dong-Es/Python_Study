import sys

repeat = int(sys.stdin.readline())

for i in range(repeat):
    a,b=map(int,sys.stdin.readline().split())

    print(a+b)