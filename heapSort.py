from animation import Plot


def createHeap(data, heapSize, index):
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2

    if left < heapSize and data[largest] < data[left]:
        largest = left

    if right < heapSize and data[largest] < data[right]:
        largest = right
    
    if largest != index:
        data[index], data[largest] = data[largest], data[index]
        createHeap(data, heapSize, largest)
        Plot(index, data)


def heapSort(data):
    heapSize = len(data)

    for i in range(heapSize//2 - 1, -1, -1):
        createHeap(data, heapSize, i)

    for i in range(heapSize-1, 0, -1):
        data[i], data[0] = data[0], data[i]
        createHeap(data, i, 0)



