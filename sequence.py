def define(flagC, flagA, flagWA, flagD, flagWD):
    if flagC:
        return 'CONSTANT'
    elif flagA:
        return 'ASCENDING'
    elif flagWA:
        return 'WEAKLY ASCENDING'
    elif flagD:
        return 'DESCENDING'
    elif flagWD:
        return 'WEAKLY DESCENDING'
    else:
        return 'RANDOM'


num = int(input())
check = num
flagC, flagA, flagWA, flagD, flagWD = True, True, True, True, True
prev = num
while num != -2e9:
    num = int(input())
    if num != -2e9:
        if num > prev:
            flagWD, flagD, flagC = False, False, False
        elif num < prev:
            flagA, flagC, flagWA = False, False, False
        else:
            flagD, flagA = False, False
        prev = num
    else:
        break

if check != -2e9:
    print(define(flagC, flagA, flagWA, flagD, flagWD))
else:
    print('RANDOM')
