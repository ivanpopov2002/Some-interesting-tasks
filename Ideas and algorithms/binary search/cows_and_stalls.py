'''На прямой расположены стойла, в которые необходимо расставить коров так, чтобы минимальное расcтояние между коровами было как можно больше.

Формат ввода
В первой строке вводятся числа N (2 < N < 10001) – количество стойл и K (1 < K < N) – количество коров. Во второй строке задаются N натуральных чисел в порядке возрастания – координаты стойл (координаты не превосходят 109)

Формат вывода
Выведите одно число – наибольшее возможное допустимое расстояние.

Ключевая идея - рассмотреть ОБРАТНУЮ задачу - найти количество коров, которых можно поместить в стойла при заданном расстоянии 

'''



def check(m, K, stalls):
    count = 1
    prev = stalls[0]
    for stall in stalls:
        if m <= stall - prev:
            count += 1
            prev = stall
    return count >= K

N, K = (int(i) for i in input().split())
stalls = list(map(int, input().split()))

l = 0
r = stalls[-1]

while l < r:
    m = (l + r + 1) // 2
    if check(m, K, stalls):
        l = m
    else:
        r = m - 1
print(l)
