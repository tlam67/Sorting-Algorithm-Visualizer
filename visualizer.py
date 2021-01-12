import algorithms
import time
import os
import sys
import pygame

dimensions = [1024, 512]

algorithms = {"QuickSort": algorithms.quickSort(), 
              "RadixSort": algorithms.radixSort(), 
              "MergeSort": algorithms.mergeSort(), 
              "HeapSort": algorithms.heapSort(), 
              "InsertionSort": algorithms.insertionSort(), 
              "SelectionSort": algorithms.selectionSort(), 
              "BubbleSort": algorithms.bubbleSort()}


if len(sys.argv) > 1:
    if sys.argv[1] == "list":
        for key in algorithms.keys(): 
            print(key, end="")
        print("")
        sys.exit(0)

pygame.init()

display = pygame.display.set_mode((dimensions[0], dimensions[1]))

display.fill(pygame.Color("#a48be0"))

def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit

def update(algorithm, swap1=None, swap2=None, display=display):
    display.fill(pygame.Color("#a48be0"))
    pygame.display.set_caption("Sorting Algorithm Visualizer       Algorithm: {}     Time: {:.3f}     Status: Sorting...".format(algorithm.name, time.time() - algorithm.start_time()))
    
    k = int(dimensions[0]/len(algorithm.array))
    
    for i in range(len(algorithm.array)):
        colour = (80, 0, 255)
        if swap1 == algorithm.array[i]:
            colour = (0, 255, 0)
        elif swap2 == algorithm.array[i]:
            colour = (255, 0, 0)

        pygame.draw.rect(display, colour, (i*k, dimensions[1], k - algorithm.array[i]))
    check_events()
    pygame.display.update()

def keep_open(algorithm, display, time):
    pygame.display.set_caption("Sorting Algorithm Visualizer       Algorithm: {}     Time: {:.3f}     Status: Sorting...".format(algorithm.name, time.time() - algorithm.start_time()))
    while True:
        check_events()
        pygame.display.update()

def main():
    if len(sys.argv) < 2:
        print("Please select a sorting algorithm.")
    else:
        try:
            algorithms = algorithms[sys.argv[1]]
            try:
                time_elapsed = algorithm.run()[1]
                keep_open(algorithm, display, time_elapsed)
                pass
            except:
                pass
        except:
            print("Error")

if __name__ == "__main":
    main()

