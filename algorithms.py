import random
import time

class Algorithm:
    def __init__(self, name):
        self.array = random.sample(range(512), 512)
        self.name = name

    def update_display(self, swap1=None, swap2=None):
        import visualizer
        visualizer.update(self, swap1, swap2)

    def run(self):
        self.start_time = time.time()
        self.algorithm()
        time_elapsed = time.time() - self.start_time
        return self.array, time_elapsed



class heapSort(Algorithm):
    def __init__(self):
        super().__init__("HeapSort")

    def algorithm(self):
        def createHeap(array, heapSize, index):
            largest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < heapSize and array[largest] < array[left]:
                largest = left

            if right < heapSize and array[largest] < array[right]:
                largest = right
            
            if largest != index:
                array[index], array[largest] = array[largest], array[index]

                createHeap(array, heapSize, largest)
        
        heapSize = len(self.array)

        for i in range(heapSize//2 - 1, -1, -1):
            createHeap(self.array, heapSize, i)

        for i in range(heapSize-1, 0, -1):
            self.array[i], self.array[0] = self.array[0], self.array[i]
            createHeap(self.array, i, 0)




heap = heapSort()
results = heap.run()
array = results[0]
time = results[1]
print("time taken: {} secs".format(time))
print("time taken: {} ms".format(time*1000))