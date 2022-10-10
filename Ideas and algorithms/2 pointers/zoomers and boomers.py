n = int(input())
numbers = [int(i) for i in input().split()]

numbers.sort()

l, r = 0, 0

count = 0

for i in range(n):
    while l < n and numbers[l] <= 0.5 * numbers[i] + 7:
        l += 1
    while r < n and numbers[r] <= numbers[i]:
        r += 1
    if l < r:
        count += r - l - 1
print(count)
