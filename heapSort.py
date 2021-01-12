import random

class heapSort(Algorithm):
    def __init__(self):
        super(),__init__("SelectionSort")

    def algorithm(self):
        heapSize = len(self.array)
        

        for i in range(heapSize//2 - 1, -1, -1):
            createHeap(array, heapSize, i)

        for i in range(heapSize-1, 0, -1):
            array[i], array[0] = array[0], array[i]
            createHeap(array, i, 0)

    def createHeap(array, heapSize, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < heapSize and array[largest] < array[left]:
            largest = left

        if right < heapSize and array[largest] < array[right]:
            largest = right
        
        if largest != index:
            array[index], array[largest] = array[largest], array[index]

            createHeap(array, heapSize, largest)


    def heapSort(array):
        heapSize = len(array)

        for i in range(heapSize//2 - 1, -1, -1):
            createHeap(array, heapSize, i)

        for i in range(heapSize-1, 0, -1):
            array[i], array[0] = array[0], array[i]
            createHeap(array, i, 0)

            

test = random.sample(range(512), 512)
heapSort(test)
print(test)