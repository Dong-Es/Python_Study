score = 0

for i in range(5):
    point=int(input())
    if point <40:
        point=40

    score += point

print(score//5)