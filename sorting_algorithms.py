import random, time
import pygame

import values as v

class Algorithm():
    def __init__(self, alg_name):
        self.name = alg_name
        self.array = random.sample(range(600), 600)

    def update(self, a=None, b=None):
        import main
        main.update_screen(self, a, b)
        
    def play(self):
        self.start_time = time.time()
        self.update()
        self.algorithm()
        self.update()

class BubbleSort(Algorithm):
    def __init__(self):
        super().__init__("BubbleSort")

    def algorithm(self):
        n = len(self.array) 
        for i in range(n-1): 
            for j in range(0, n-i-1): 
                if self.array[j] > self.array[j+1] : 
                    self.array[j], self.array[j+1] = self.array[j+1], self.array[j]
                self.update(self.array[j], self.array[j-1])

class QuickSort(Algorithm):
    def __init__(self):
        super().__init__("QuickSort")

    def algorithm(self):
        # Hoare partition scheme
        def _quicksort(low, high):
            if low < high: 
                p = partition(low, high)
                _quicksort(low, p)
                _quicksort(p+1, high)

        def partition(low, high):
            pivot = self.array[low]
            while True:
                while self.array[low] < pivot:
                    low += 1
                while self.array[high] > pivot:
                    high -= 1
                if low >= high:
                    return high
                self.array[low], self.array[high] = self.array[high], self.array[low]
                low += 1
                high -= 1
                self.update(self.array[low], self.array[high])
        _quicksort(0, len(self.array)-1)
        #return self.update()

class InsertionSort(Algorithm):
    def __init__(self):
        super().__init__("InsertionSort")

    def algorithm(self):
        for i in range(1, len(self.array)): 
            key = self.array[i] 
            j = i-1
            while j >= 0 and key < self.array[j] : 
                    self.array[j+1] = self.array[j] 
                    j -= 1
            self.array[j+1] = key
            self.update(key, j)

# Don't try this one
class BogoSort(Algorithm):
    def __init__(self):
        super().__init__("BogoSort")

    def algorithm(self):
        def _bogosort():
            random.shuffle(self.array)
            for i, j in enumerate(self.array):
                if i != j:
                    self.update(i, j)
                    time.sleep(0.01)
                    _bogosort()
        _bogosort()
