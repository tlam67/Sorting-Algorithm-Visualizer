from animation import Plot

def partition(array, low, high):
    i = (low - 1)
    pivot = array[high]

    for j in range(low, high):
        if array[j] < pivot:
            i+= 1
            array[i], array[j] = array[j], array[i]
            Plot(i+1, array)
        
    array[i+1], array[high] = array[high], array[i+1]
    return i+1

def quickSort(array, low, high):
    if low < high:
        pIndex = partition(array, low, high)
        quickSort(array, low, pIndex-1)
        quickSort(array, pIndex+1, high)
    return array
