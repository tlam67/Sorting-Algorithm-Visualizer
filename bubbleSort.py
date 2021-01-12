import random

def bubbleSort(array):
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array


test = random.sample(range(512), 512)
print(bubbleSort(test))