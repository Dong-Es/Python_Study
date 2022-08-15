import sys
text = sys.stdin.readline().rstrip()
result=[0]*(26)

for word in text:
    result[ord(word)-97] +=1

print(*result)
#