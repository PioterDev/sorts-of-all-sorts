#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <windows.h>

#include "additional.h"
#include "heapsort.h"
#include "mergesort.h"
#include "quicksort.h"
#include "shellsort.h"

//typedef struct timespec time;

long long test(char algorithm, int* testArr, int size, char printStuff) {
    LARGE_INTEGER start, end;
    switch (algorithm) {
        case 'm':
            if(printStuff)printf("Merge sort\n");
            int* arrMerge = copy(testArr, size);
            QueryPerformanceCounter(&start);
            mergeSort(arrMerge, 0, size - 1);
            QueryPerformanceCounter(&end);
            if(printStuff)printf("Time taken to sort: %ld\n", end.QuadPart - start.QuadPart);
            free(arrMerge);
            return end.QuadPart - start.QuadPart;

        case 'h':
            if(printStuff)printf("Heap sort\n");
            int* arrHeap = copy(testArr, size);
            QueryPerformanceCounter(&start);
            heapSort(arrHeap, size - 1);
            QueryPerformanceCounter(&end);
            if(printStuff)printf("Time taken to sort: %ld\n", end.QuadPart - start.QuadPart);
            free(arrHeap);
            return end.QuadPart - start.QuadPart;

        case 's':
            if(printStuff)printf("Shell sort\n");
            int* arrShell = copy(testArr, size);
            QueryPerformanceCounter(&start);
            shellSort(arrShell, size - 1, printStuff);
            QueryPerformanceCounter(&end);
            if(printStuff)printf("Time taken to sort: %ld\n", end.QuadPart - start.QuadPart);
            free(arrShell);
            return end.QuadPart - start.QuadPart;

        case 'r':
            if(printStuff)printf("Quick sort - recursive\n");
            int* arrQuickRecursive = copy(testArr, size);
            QueryPerformanceCounter(&start);
            quickSort(arrQuickRecursive, 0, size - 1, 0);
            QueryPerformanceCounter(&end);
            if(printStuff)printf("Time taken to sort: %ld\n", end.QuadPart - start.QuadPart);
            free(arrQuickRecursive);
            return end.QuadPart - start.QuadPart;

        case 'i':
            if(printStuff)printf("Quick sort - iterative\n");
            int* arrQuickIterative = copy(testArr, size);
            QueryPerformanceCounter(&start);
            quickSortIterative(arrQuickIterative, 0, size - 1, 0);
            QueryPerformanceCounter(&end);
            if(printStuff)printf("Time taken to sort: %ld\n", end.QuadPart - start.QuadPart);
            free(arrQuickIterative);
            return end.QuadPart - start.QuadPart;
            
        default:
            return 0;
    }
}