from animation import Plot

def countingSort(array, digit):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    for i in range(0, size):
        index = array[i]//digit
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        index = array[i] // digit
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        Plot(i, array)
        i -= 1

    for i in range(0, size):
        array[i] = output[i]
        Plot(i, array)
    #Plot(len(array)-1, array)

def radixSort(array):
    maxElement = max(array)

    digit = 1
    while maxElement // digit > 0:
        countingSort(array, digit)
        digit *= 10
    

