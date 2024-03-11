import time
from sort.bubblesort import bubbleSort
from sort.mergesort import mergeSort
from sort.heapsort import heapSort
from sort.quicksort import quickSortRecursive, quickSortIterative
from sort.insertionsort import insertionSort, insertionSortWithReturn
from sort.shellsort import shellSort
from rng import *

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
            sortedMerge = mergeSort(lMerge, printMergeNum=True)
            finish = time.time_ns() - start
            print(f"Time taken to sort: {finish/(10**9)}s")
            return finish
        case "quick-recursive":
            print("Quick sort - recursive version")
            lQuick = testList.copy()
            start = time.time_ns()
            quickSortRecursive(lQuick, 0, len(lQuick) - 1)
            finish = time.time_ns() - start
            print(f"Time taken to sort: {finish/(10**9)}s")
            return finish
        case "heap":
            print("Heap sort")
            lHeap = testList.copy()
            start = time.time_ns()
            heapSort(lHeap)
            finish = time.time_ns() - start
            print(f"Time taken to sort: {finish/(10**9)}s")
            return finish
        case "bubble":
            print("Bubble sort")
            lBubble = testList.copy()
            start = time.time_ns()
            bubbleSort(lBubble)
            finish = time.time_ns() - start
            print(f"Time taken to sort: {finish/(10**9)}s")
            return finish
        case "quick-iterative":
            print("Quick sort - iterative version")
            lQuick = testList.copy()
            start = time.time_ns()
            quickSortIterative(lQuick, 0, len(lQuick) - 1)
            finish = time.time_ns() - start
            print(f"Time taken to sort: {finish/(10**9)}s")
            return finish
        case "insert":
            print("Insertion sort")
            lInsert = testList.copy()
            start = time.time_ns()
            insertionSort(lInsert)
            finish = time.time_ns() - start
            print(f"Time taken to sort: {finish/(10**9)}s")
            return finish
        case "tim":
            print("Python's Tim sort")
            lTim = testList.copy()
            start = time.time_ns()
            lTim.sort()
            finish = time.time_ns() - start
            print(f"Time taken to sort: {finish/(10**9)}s")
            return finish
        case "shell":
            print("Shell sort - insertion sort as base, Hibbard's numbers as increments")
            lShell = testList.copy()
            start = time.time_ns()
            shellSort(lShell)
            finish = time.time_ns() - start
            print(f"Time taken to sort: {finish/(10**9)}s")
            return finish
         
#l = losowe(100_000_000)
'''
test("heap", l)
test("merge", l)
test("quick-recursive", l)
test("quick-iterative", l)
test("insert", l)
test("shell", l)
'''