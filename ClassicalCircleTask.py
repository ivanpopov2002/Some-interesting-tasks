def convert(s):
    h, m = (int(i) for i in s.split(':'))
    return h * 60 + m

n = int(input())
lst = list(map(convert, input().split()))
lst.sort()
minDist = 1440 + lst[0] - lst[-1]

for i in range(1, len(lst)):
    minDist = min(minDist, lst[i] - lst[i - 1])

print(minDist)
