from animation import Plot

def insertionSort(data):
    for i in range(len(data)):
        current = data[i]
        index = i
        while index > 0 and data[index-1] > current:
            data[index] = data[index-1]
            index -= 1
            Plot(index, data)
        data[index] = current
    return data
