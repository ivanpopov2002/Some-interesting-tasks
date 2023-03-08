N = int(input())

heap = []

def insert(value):
    '''Вставка элемента в кучу'''
    heap.append(value)
    pos = len(heap) - 1
    while pos > 0 and heap[pos] > heap[(pos - 1) // 2]:
        heap[pos], heap[(pos - 1) // 2] = heap[(pos - 1) // 2], heap[pos]
        pos = (pos - 1) // 2

def extract():
  '''Удаление максимального элемента в куче'''
    ans = heap[0]
    heap[0] = heap[-1]
    pos = 0
    while pos * 2 + 1 < len(heap) - 1:
        max_son_index = pos * 2 + 1
        if heap[pos * 2 + 2] > heap[max_son_index]:
            max_son_index = pos * 2 + 2
        if heap[pos] < heap[max_son_index]:
            heap[pos], heap[max_son_index] = heap[max_son_index], heap[pos]
            pos = max_son_index
        else:
            break
    heap.pop()
    return ans

for _ in range(N):
    command = list(map(int, input().split()))
    if command[0] == 0:
        insert(command[1])
    else:
        print(extract())
