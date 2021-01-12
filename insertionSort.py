import random

def insertionSort(array):
    for i in range(len(array)):
        current = array[i]
        index = i
        while index > 0 and array[index-1] > current:
            array[index] = array[index-1]
            index -= 1
        array[index] = current
    return array

test = random.sample(range(512), 512)
print(insertionSort(test))