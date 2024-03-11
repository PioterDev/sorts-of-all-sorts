import time
from .sort.bubblesort import bubbleSort
from .sort.mergesort import mergeSort
from .sort.heapsort import heapSort
from .sort.quicksort import quickSortRecursive, quickSortIterative
from .sort.insertionsort import insertionSort, insertionSortWithReturn
from .sort.shellsort import shellSort

def isSorted(l:list, reverse=False) -> bool:
    for i in range(1, len(l)):
        if reverse:
            if l[i] > l[i - 1]:
                return False
        else:
            if l[i - 1] > l[i]:
                return False
    return True

def test(name: str, testList: list[int]) -> None:
    match name:
        case "merge":
            print("Merge sort")
            lMerge = testList.copy()
            start = time.time_ns()
            sortedMerge = mergeSort(lMerge)
            finish = (time.time_ns() - start)/(10 ** 9)
            print(f"Time taken to sort: {finish}s")
            return lMerge
        case "quick-recursive":
            print("Quick sort - recursive version")
            lQuick = testList.copy()
            start = time.time_ns()
            quickSortRecursive(lQuick, 0, len(lQuick) - 1)
            finish = (time.time_ns() - start)/(10 ** 9)
            print(f"Time taken to sort: {finish}s")
            return lQuick
        case "heap":
            print("Heap sort")
            lHeap = testList.copy()
            start = time.time_ns()
            heapSort(lHeap)
            finish = (time.time_ns() - start)/(10 ** 9)
            print(f"Time taken to sort: {finish}s")
            return lHeap
        case "bubble":
            print("Bubble sort")
            lBubble = testList.copy()
            start = time.time_ns()
            bubbleSort(lBubble)
            finish = (time.time_ns() - start)/(10 ** 9)
            print(f"Time taken to sort: {finish}s")
            return lBubble
        case "quick-iterative":
            print("Quick sort - iterative version")
            lQuick = testList.copy()
            start = time.time_ns()
            quickSortIterative(lQuick, 0, len(lQuick) - 1)
            finish = (time.time_ns() - start)/(10 ** 9)
            print(f"Time taken to sort: {finish}s")
            return lQuick
        case "insert":
            print("Insertion sort")
            lInsert = testList.copy()
            start = time.time_ns()
            insertionSort(lInsert)
            finish = (time.time_ns() - start)/(10 ** 9)
            print(f"Time taken to sort: {finish}s")
            return lInsert
        case "tim":
            print("Python's Tim sort")
            lTim = testList.copy()
            start = time.time_ns()
            lTim.sort()
            finish = (time.time_ns() - start)/(10 ** 9)
            print(f"Time taken to sort: {finish}s")
            return lTim
        case "shell":
            print("Shell sort - insertion sort as base, Hibbard's numbers as increments")
            lShell = testList.copy()
            start = time.time_ns()
            shellSort(lShell)
            finish = (time.time_ns() - start)/(10 ** 9)
            print(f"Time taken to sort: {finish}s")
            return lShell
        
'''
l = [random.randint(0, 100_000_000) for i in range(1_000_000)]
testSortingAlgorithm("heap", l)
testSortingAlgorithm("merge", l)
testSortingAlgorithm("quick-recursive", l)
testSortingAlgorithm("quick-iterative", l)
testSortingAlgorithm("insert", l)
testSortingAlgorithm("shell", l)
'''