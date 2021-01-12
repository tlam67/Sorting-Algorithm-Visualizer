import random

def selectionSort(array):
    for i in range(len(array)):
        index = i
        for j in range(i+1, len(array)):
            if array[index] > array[j]:
                index = j
        array[i], array[index] = array[index], array[i]
    return array

test = random.sample(range(512), 512)
print(selectionSort(test))