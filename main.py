import math
import random
import time
import sys
from sort.bubblesort import bubbleSort
from sort.mergesort import mergeSort
from sort.heapsort import heapSort
from sort.quicksort import quickSortRecursive, quickSortIterative
from sort.insertionsort import insertionSort

sys.setrecursionlimit(10**6)

def testSortingAlgorithm(name: str, testList: list):
    match name:
        case "merge":
            print("Merge sort")
            lMerge = testList.copy()
            start = time.time_ns()
            sortedMerge = mergeSort(lMerge)
            finish = (time.time_ns() - start)/(10 ** 9)
            print(f"Time taken to sort: {finish}s")
        case "quick-recursive":
            print("Quick sort - recursive version")
            lQuick = testList.copy()
            start = time.time_ns()
            quickSortRecursive(lQuick, 0, len(lQuick) - 1)
            finish = (time.time_ns() - start)/(10 ** 9)
            print(f"Time taken to sort: {finish}s")
        case "heap":
            print("Heap sort")
            lHeap = testList.copy()
            start = time.time_ns()
            heapSort(lHeap)
            finish = (time.time_ns() - start)/(10 ** 9)
            print(f"Time taken to sort: {finish}s")
        case "bubble":
            print("Bubble sort")
            lBubble = testList.copy()
            start = time.time_ns()
            bubbleSort(lBubble)
            finish = (time.time_ns() - start)/(10 ** 9)
            print(f"Time taken to sort: {finish}s")
        case "quick-iterative":
            print("Quick sort - iterative version")
            lQuick = testList.copy()
            start = time.time_ns()
            quickSortIterative(lQuick, 0, len(lQuick) - 1)
            finish = (time.time_ns() - start)/(10 ** 9)
            print(f"Time taken to sort: {finish}s")
        case "insert":
            print("Insertion sort")
            lInsert = testList.copy()
            start = time.time_ns()
            insertionSort(lInsert)
            finish = (time.time_ns() - start)/(10 ** 9)
            print(f"Time taken to sort: {finish}s")
        case "tim":
            print("Python's Tim sort")
            lTim = testList.copy()
            start = time.time_ns()
            lTim.sort()
            finish = (time.time_ns() - start)/(10 ** 9)
            print(f"Time taken to sort: {finish}s")

l = [random.randint(0, 100_000_000) for i in range(1_000_000)]
#rev = False
#print("Sorting in reverse: ", rev)
#'''
testSortingAlgorithm("heap", l)
testSortingAlgorithm("merge", l)
testSortingAlgorithm("quick-recursive", l)
testSortingAlgorithm("quick-iterative", l)
testSortingAlgorithm("insert", l)
#'''
