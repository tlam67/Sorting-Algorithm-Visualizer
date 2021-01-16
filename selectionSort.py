from animation import Plot

def selectionSort(data):
    for i in range(len(data)):
        index = i
        for j in range(i+1, len(data)):
            if data[index] > data[j]:
                index = j
            Plot(j, data)

        data[i], data[index] = data[index], data[i]
    return data
