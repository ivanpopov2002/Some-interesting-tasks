'''Вам необходимо ответить на запросы узнать сумму всех элементов
числовой матрицы N×M в прямоугольнике 
с левым верхним углом (x1, y1) и правым нижним (x2, y2)'''

n, m, k = list(map(int, input().split()))
matrix = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if i:
            matrix[i][j] += matrix[i - 1][j]
        if j:
            matrix[i][j] += matrix[i][j - 1]
        if i and j:
            matrix[i][j] -= matrix[i - 1][j - 1]

for _ in range(k):
    x1, y1, x2, y2 = list(map(lambda x: int(x) - 1, input().split()))
    if x1 and y1:
        print(matrix[x2][y2] - matrix[x1 - 1][y2] - matrix[x2][y1 - 1] + matrix[x1 - 1][y1 - 1])
    elif x1:
        print(matrix[x2][y2] - matrix[x1 - 1][y2])
    elif y1:
        print(matrix[x2][y2] - matrix[x2][y1 - 1])
    else:
        print(matrix[x2][y2])
