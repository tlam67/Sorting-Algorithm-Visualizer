import random
#import quickSort, mergeSort, heapSort, radixSort,insertionSort, selectionSort
from selectionSort import selectionSort
from bubbleSort import bubbleSort
from heapSort import heapSort
from insertionSort import insertionSort
from mergeSort import mergeSort
from quickSort import quickSort
from radixSort import radixSort
from animation import camera, algorithm_title, graph_title, graphs
import matplotlib.pyplot as plt


# get the size of the data that the user wants
# get the algo they want
# get the plot they want
# get the graph title and algorithm title
# apply algorithm
# set interval time for camera animation
# show the plot

def determine_data_size():
    try:
        
        size = input('Size of the array to be sorted: ')

        size = int(size)

        if size <= 0:
            print('Invalid data size, try again')
            determine_data_size()
        else:
            return size
    except ValueError:
        print('Invalid data size, must be integer. Try again')
        determine_data_size()


size = determine_data_size()
print(size)

data = random.sample(range(size), size)

algorithms = {
    '1': quickSort, 
    '2': mergeSort, 
    '3': heapSort, 
    '4': radixSort, 
    '5': insertionSort, 
    '6': selectionSort, 
    '7': bubbleSort,
    'QuickSort': quickSort, 
    'MergeSort': mergeSort, 
    'HeapSort': heapSort, 
    'RadixSort': radixSort, 
    'InsertionSort': insertionSort, 
    'SelectionSort': selectionSort,
    'BubbleSort': bubbleSort
}


def determine_algorithm():
    try:
        algo = input("Select the algorithm:\n1: QuickSort\n2: MergeSort\n3: HeapSort\n4: RadixSort\n5: InsertionSort\n6: SelectionSort\n7: BubbleSort\n")

        if algo not in algorithms:
            print("Invalid choice. Try again.")
            determine_algorithm()
        
        return algo
    except:
        print('Error')


algorithm_choice = determine_algorithm()

algorithm = algorithms[algorithm_choice]
#print(algorithm)
algorithm_title(algorithm_choice)

def determine_plot():
    try:
        plot_type = input("Select the plot type:\n1: Bar Plot\n2: Scatter Plot\n")

        if plot_type not in graphs:
            print("Invalid choice. Try again.")
            determine_plot()

        return plot_type
    except:
        print('Error')

plot_choice = determine_plot()

plot = graphs[plot_choice]
print(plot)
graph_title(plot_choice)


if algorithm == quickSort:
    algorithm(data, 0, len(data) - 1)
else:
    algorithm(data)
#algorithm(data)

animation = camera.animate()

#animation.save('sorting.mp4', fps=20)

plt.show()



