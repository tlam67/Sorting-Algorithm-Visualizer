import matplotlib
import matplotlib.pyplot as plt
from celluloid import Camera

fig = plt.figure()
camera = Camera(fig)

comparisons = 0

titles = {
    '1': "QuickSort", 
    '2': "MergeSort", 
    '3': "HeapSort", 
    '4': "RadixSort", 
    '5': "InsertionSort", 
    '6': "SelectionSort", 
    '7': "BubbleSort",
    'QuickSort': "QuickSort", 
    'MergeSort': "MergeSort", 
    'HeapSort': "HeapSort", 
    'RadixSort': "RadixSort", 
    'InsertionSort': "InsertionSort", 
    'SelectionSort': "SelectionSort",
    'BubbleSort': "BubbleSort"
}

graphs = {
    '1': plt.bar, 
    '2': plt.scatter
}


def algorithm_title(algorithm):
    global title
    title = titles[algorithm]
    return title

def graph_title(grph):
    global graph
    graph = graphs[grph]
    return graph



def Plot(highlight, data):
    coords = list(range(len(data)))

    #increment comparisons
    global comparisons
    comparisons += 1

    colors = list(len(data) * 'g') #set default bar color to blue
    colors[highlight] = 'r' #set highlight bar color to red'
    
    if graph == plt.bar:
        graph(coords, data, data=data, color=colors) #graph the plot
    elif graph == plt.scatter:
        graph(coords, data, c=data) #coords = x, data = y, c=colours

    plt.title(title) #give plot the proper title based on algorithm being used
    #plt.xlabel('Data size: {}, Comparisons: {}'.format(len(data), comparisons)) #label the plot
    plt.xlabel('Data size: {}'.format(len(data)))

    camera.snap() #take snapshot to use for animation

