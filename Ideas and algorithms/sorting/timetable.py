table = list()
for _ in range(int(input())):
    lesson_start, lesson_end = (int(i) for i in input().split())
    table.append([lesson_start, lesson_end])

table.sort(key=lambda x: x[1])

cnt = 0
t = 0

for lesson in table:
    if lesson[0] >= t:
        cnt += 1
        t = lesson[1]
print(cnt)
