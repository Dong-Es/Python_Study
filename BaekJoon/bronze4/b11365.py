import sys

while(True):
    text=(sys.stdin.readline().rstrip())
    if text == "END":
        break
    print(text[::-1])