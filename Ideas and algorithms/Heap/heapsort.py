N = int(input())

arr = [int(i) for i in input().split()]        

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def siftDown(arr, i, upper):
    while True:
        l, r = i * 2 + 1, i * 2 + 2
        if max(l, r) < upper:
            if arr[i] >= max(arr[l], arr[r]):
                break
            elif arr[l] > arr[r]:
                swap(arr, i, l)
                i = l
            else:
                swap(arr, i, r)
                i = r
        elif l < upper:
            if arr[l] > arr[i]:
                swap(arr, i, l)
                i = l
            else:
                break
        else:
            break
            


def heapsort(arr):
    #получаем кучу с максимумом в первой вершине
    for j in range((len(arr) - 2) // 2, -1, -1):
        siftDown(arr, j, len(arr))
    #начинаем сортировку
    for end in range(len(arr) - 1, 0, -1):
        swap(arr, 0, end)
        siftDown(arr, 0, end)

heapsort(arr)
print(*arr)
