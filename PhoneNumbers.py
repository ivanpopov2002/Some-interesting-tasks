n1 = input().replace('-', '').replace('(', '').replace(')', '')
n2 = input().replace('-', '').replace('(', '').replace(')', '')
n3 = input().replace('-', '').replace('(', '').replace(')', '')
n4 = input().replace('-', '').replace('(', '').replace(')', '')

lst = [n1, n2, n3, n4]

for i in range(4):
    if lst[i][:2] == '+7':
        lst[i] = lst[i].replace('+7', '8')
    if len(lst[i]) == 7:
        lst[i] = '8495' + lst[i]
    print(lst[i])

for i in range(1, 4):
    if lst[i] == lst[0]:
        print('YES')
    else:
        print('NO')
