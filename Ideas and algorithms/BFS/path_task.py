'''Пещера представлена кубом, разбитым на N частей по каждому измерению 
(то есть на N3 кубических клеток). Каждая клетка может быть или пустой, или полностью заполненной камнем. 
Исходя из положения спелеолога в пещере, требуется найти, какое минимальное количество перемещений по клеткам ему требуется, 
чтобы выбраться на поверхность. Переходить из клетки в клетку можно, только если они обе свободны и имеют общую грань.

Формат ввода
В первой строке содержится число N (1 ≤ N ≤ 30). Далее следует N блоков. 
Блок состоит из пустой строки и N строк по N символов: # - обозначает клетку, 
заполненную камнями, точка - свободную клетку. Начальное положение спелеолога обозначено заглавной буквой S. 
Первый блок представляет верхний уровень пещеры, достижение любой свободной его клетки означает выход на поверхность. 
Выход на поверхность всегда возможен.

Формат вывода
Вывести одно число - длину пути до поверхности.

Пример
Ввод
3

###
###
.##

.#.
.#S
.#.

###
...
###
Вывод
6'''


from collections import deque
import sys

queue = deque()
rows = []
for line in sys.stdin.readlines():
    if line.strip():
        rows.append(line.strip())

n = int(rows[0])
rows = rows[1:]

matrix = [[[None] * n for _ in range(n)] for _ in range(n)]

count = 0

for row in rows:
    for j in range(n):
        if row[j] == '#':
            matrix[count // n][count % n][j] = 'blocked'
        elif row[j] == '.':
            matrix[count // n][count % n][j] = 'vacant'
        else:
            matrix[count // n][count % n][j] = 0
            a, b, c = count // n, count % n, j
    count += 1
    

queue.append((a, b, c))

while queue:
    x, y, z = queue.popleft()
    if x == 0:
        print(matrix[x][y][z])
        break
    upper = x - 1
    lower = x + 1
    left = z - 1
    up = y - 1
    down = y + 1
    right = z + 1
    if upper >= 0 and matrix[upper][y][z] == 'vacant':
        matrix[upper][y][z] = matrix[x][y][z] + 1
        queue.append((upper, y, z))
    if lower < len(matrix) and matrix[lower][y][z] == 'vacant':
        matrix[lower][y][z] = matrix[x][y][z] + 1
        queue.append((lower, y, z))
    if left >= 0 and matrix[x][y][left] == 'vacant':
        matrix[x][y][left] = matrix[x][y][z] + 1
        queue.append((x, y, left))
    if right < n and matrix[x][y][right] == 'vacant':
        matrix[x][y][right] = matrix[x][y][z] + 1
        queue.append((x, y, right))
    if up >= 0 and matrix[x][up][z] == 'vacant':
        matrix[x][up][z] = matrix[x][y][z] + 1
        queue.append((x, up, z))
    if down < len(matrix) and matrix[x][down][z] == 'vacant':
        matrix[x][down][z] = matrix[x][y][z] + 1
        queue.append((x, down, z))
