import time, sys
from sort.bubblesort import bubbleSort
from sort.mergesort import mergeSort
from sort.heapsort import heapSort
from sort.quicksort import quickSortRecursive, quickSortIterative
from sort.insertionsort import insertionSort, insertionSortWithReturn
from sort.shellsort import shellSort
from rng import *

sys.setrecursionlimit(10 ** 6)

def isSorted(l:list, reverse=False) -> bool:
    for i in range(1, len(l)):
        if reverse:
            if l[i] > l[i - 1]:
                return False
        else:
            if l[i - 1] > l[i]:
                return False
    return True

def test(name: str, testList: list[int], lang="eng", reverse=False, printTime=True):
    match name:
        case "merge":
            print("Merge sort")
            lMerge = testList.copy()
            start = time.time_ns()
            sortedMerge = mergeSort(lMerge, reverse, printMergeNum=True, lang="pl")
            finish = time.time_ns() - start
            if printTime:    
                if lang == "pl":
                    print(f"Czas potrzebny do posortowania: {finish/(10**9)}")
                else: print(f"Time taken to sort: {finish/(10**9)}s")
            return finish
        case "quick-recursive":
            if lang == "pl":
                print("Quick sort - wersja rekurencyjna")
            else: print("Quick sort - recursive version")
            lQuick = testList.copy()
            start = time.time_ns()
            quickSortRecursive(lQuick, 0, len(lQuick) - 1, reverse)
            finish = time.time_ns() - start
            if printTime:
                if lang == "pl":
                    print(f"Czas potrzebny do posortowania: {finish/(10**9)}")
                else: print(f"Time taken to sort: {finish/(10**9)}s")
            return finish
        case "heap":
            print("Heap sort")
            lHeap = testList.copy()
            start = time.time_ns()
            heapSort(lHeap, reverse)
            finish = time.time_ns() - start
            if printTime:
                if lang == "pl":
                    print(f"Czas potrzebny do posortowania: {finish/(10**9)}")
                else: print(f"Time taken to sort: {finish/(10**9)}s")
            return finish
        case "bubble":
            print("Bubble sort")
            lBubble = testList.copy()
            start = time.time_ns()
            bubbleSort(lBubble, reverse)
            finish = time.time_ns() - start
            if printTime:
                if lang == "pl":
                    print(f"Czas potrzebny do posortowania: {finish/(10**9)}")
                else: print(f"Time taken to sort: {finish/(10**9)}s")
            return finish
        case "quick-iterative":
            if lang == "pl":
                print("Quick sort - wersja iteracyjna")
            else: print("Quick sort - iterative version")
            lQuick = testList.copy()
            start = time.time_ns()
            quickSortIterative(lQuick, 0, len(lQuick) - 1, reverse)
            finish = time.time_ns() - start
            if printTime:
                if lang == "pl":
                    print(f"Czas potrzebny do posortowania: {finish/(10**9)}")
                else: print(f"Time taken to sort: {finish/(10**9)}s")
            return finish
        case "insert":
            print("Insertion sort")
            lInsert = testList.copy()
            start = time.time_ns()
            insertionSort(lInsert, reverse)
            finish = time.time_ns() - start
            if printTime:
                if lang == "pl":
                    print(f"Czas potrzebny do posortowania: {finish/(10**9)}")
                else: print(f"Time taken to sort: {finish/(10**9)}s")
            return finish
        case "tim":
            if lang == "pl":
                print("Pythonowy Tim sort")
            else: print("Python's Tim sort")
            lTim = testList.copy()
            start = time.time_ns()
            lTim.sort(reverse)
            finish = time.time_ns() - start
            if printTime:
                if lang == "pl":
                    print(f"Czas potrzebny do posortowania: {finish/(10**9)}")
                else: print(f"Time taken to sort: {finish/(10**9)}s")
            return finish
        case "shell":
            if lang == "pl":
                print("Shell sort - algorytm bazowy: insertion sort przyrosty Hibbarda")
            else: print("Shell sort - insertion sort as base, Hibbard's numbers as increments")
            lShell = testList.copy()
            start = time.time_ns()
            shellSort(lShell, reverse)
            finish = time.time_ns() - start
            if printTime:
                if lang == "pl":
                    print(f"Czas potrzebny do posortowania: {finish/(10**9)}")
                else: print(f"Time taken to sort: {finish/(10**9)}s")
            return finish

'''
f = open("./testList.txt", "w")
l = losowe(10_000_000)
for i in range(len(l)):
    l[i] = str(l[i])
f.write(str(len(l)) + "\n" + "\n".join(l))
f.close()
#l = losowe(100_000_000)
'''
'''
test("heap", l)
test("merge", l)
test("quick-recursive", l)
test("quick-iterative", l)
test("insert", l)
test("shell", l)
'''