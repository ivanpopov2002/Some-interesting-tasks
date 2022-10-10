n = int(input())
numbers = list(map(int, input().split()))

prPos = [0]

for i in range(n):
    if numbers[i] > 0:
        prPos.append(prPos[-1] + 1)
    else:
        prPos.append(prPos[-1])

q = int(input())
for i in range(q):
    l, r = (int(i) for i in input().split())
    print(prPos[r] - prPos[l - 1])
