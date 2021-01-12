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


class radixSort(Algorithm):
    def __init__(self):
        super().__init__("RadixSort")

    def algorithm(self):
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
                i -= 1

            for i in range(0, size):
                array[i] = output[i]
        
        maxElement = max(self.array)

        digit = 1
        while maxElement // digit > 0:
            countingSort(self.array, digit)
            digit *= 10


class mergeSort(Algorithm):
    def __init__(self):
        super().__init__("MergeSort")

    def algorithm(self):
        def merge(array):
            if len(array) > 1:
                mid = len(array)//2
                left = array[:mid]
                right = array[mid:]
                
                merge(left)
                merge(right)

                i = j = k = 0

                while i < len(left) and j < len(right):
                    if left[i] < right[j]:
                        array[k] = left[i]
                        i += 1
                    else:
                        array[k] = right[j]
                        j += 1
                    k += 1
                
                while i < len(left):
                    array[k] = left[i]
                    i += 1
                    k += 1

                while j < len(right):
                    array[k] = right[j]
                    j += 1
                    k += 1
        
        merge(self.array)


class quickSort(Algorithm):
    def __init__(self):
        super().__init__("QuickSort")

    def algorithm(self):
        def partition(array, low, high):
            i = (low - 1)
            pivot = array[high]

            for j in range(low, high):
                if array[j] < pivot:
                    i+= 1
                    array[i], array[j] = array[j], array[i]
            array[i+1], array[high] = array[high], array[i+1]
            return i+1

        def quick(array, low, high):
            if low < high:  
                pIndex = partition(array, low, high)
                quick(array, low, pIndex-1)
                quick(array, pIndex+1, high)

        quick(self.array, 0, len(self.array)-1)
            
class selectionSort(Algorithm):
    def __init__(self):
        super().__init__("SelectionSort")

    def algorithm(self):
        for i in range(len(self.array)):
            index = i
            for j in range(i+1, len(self.array)):
                if self.array[index] > self.array[j]:
                    index = j
            self.array[i], self.array[index] = self.array[index], self.array[i]

class bubbleSort(Algorithm):
    def __init__(self):
        super().__init__("BubbleSort")

    def algorithm(self):
        for i in range(len(self.array)):
            for j in range(len(self.array)-i-1):
                if self.array[j] > self.array[j+1]:
                    self.array[j], self.array[j+1] = self.array[j+1], self.array[j]

class insertionSort(Algorithm):
    def __init__(self):
        super().__init__("InsertionSort")

    def algorithm(self):
        for i in range(len(self.array)):
            current = self.array[i]
            index = i
            while index > 0 and self.array[index-1] > current:
                self.array[index] = self.array[index-1]
                index -= 1
            self.array[index] = current

heap = heapSort()
heapResults = heap.run()
heapArray = heapResults[0]
heapTime = heapResults[1]
print("time taken: {} secs".format(heapTime))
print("time taken: {} ms".format(heapTime*1000))

radix = radixSort()
radixResults = radix.run()
radixArray = radixResults[0]
radixTime = radixResults[1]
print("time taken: {} secs".format(radixTime))
print("time taken: {} ms".format(radixTime*1000))

merge = mergeSort()
mergeResults = merge.run()
mergeArray = mergeResults[0]
mergeTime = mergeResults[1]
print("time taken: {} secs".format(mergeTime))
print("time taken: {} ms".format(mergeTime*1000))


quick = quickSort()
quickResults = quick.run()
quickArray = quickResults[0]
quickTime = quickResults[1]
print("time taken: {} secs".format(quickTime))
print("time taken: {} ms".format(quickTime*1000))


selection = selectionSort()
selectionResults = selection.run()
selectionArray = selectionResults[0]
selectionTime = selectionResults[1]
print("time taken: {} secs".format(selectionTime))
print("time taken: {} ms".format(selectionTime*1000))

bubble = bubbleSort()
bubbleResults = bubble.run()
bubbleArray = bubbleResults[0]
bubbleTime = bubbleResults[1]
print("time taken: {} secs".format(bubbleTime))
print("time taken: {} ms".format(bubbleTime*1000))

insertion = insertionSort()
insertionResults = insertion.run()
insertionArray = insertionResults[0]
insertionTime = insertionResults[1]
print("time taken: {} secs".format(insertionTime))
print("time taken: {} ms".format(insertionTime*1000))