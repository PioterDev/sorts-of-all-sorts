#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <windows.h>

#include "additional.h"
#include "insertionsort.h"
#include "rng.h"

int lenSliced(int n, int start, int step) {
    int j = 0;
    for(int i = start; i < n; i += step) j++;
    return j;
}

int* slice(int arr[], int n, int start, int step) {
    int k = 0;
    int* sliced = malloc(sizeof(int) * lenSliced(n, start, step));
    int i = 0;
    for(i = start; i < n; i += step)sliced[k++] = arr[i];
    return sliced;
}

void join(int arr[], int n, int step, int** arrays) {
    for(int i = 0; i < step; i++) {
        int k = i;
        for(int j = 0; j < lenSliced(n, i, step); j++) {
            arr[k] = arrays[i][j];
            k += step;
        }
    }
}

int hibbard(int k) {
    return (int) pow(2, k) - 1;
}

double hibbardInverse(int y) {
    return log2(y + 1);
}

void shellSort(int arr[], int n, char print) {
    int k = (int) (floor(hibbardInverse(n))) - 4;
    if(k < 0)k = 2;
    int H = hibbard(k);
    while(H >= 1) {
        if(print)printf("Current Hibbard's number: %d\n", H);
        for(int i = 0; i < H; i++) {
            insertionSort(arr, n, i, H);
        }
        k--;
        H = hibbard(k);
    }
}

/* int main() {
    LARGE_INTEGER start, end, frequency;
    QueryPerformanceFrequency(&frequency);

    int n = 100000;
    int* test = malejace(n);
    //printArray(test, n);
    FILE* unsorted = fopen("./unsorted.txt", "w");
    for(int i = 0; i < n; i++) {
        fprintf(unsorted, "%d\n", test[i]);
    }
    fclose(unsorted);
    QueryPerformanceCounter(&start);
    shellSort(test, n, 1);
    QueryPerformanceCounter(&end);
    FILE* sorted = fopen("./sorted.txt", "w");
    for(int i = 0; i < n; i++) {
        fprintf(sorted, "%d\n", test[i]);
    }
    fclose(sorted);
    printf("%ld\n", end.QuadPart - start.QuadPart);
    //printArray(test, n);
    return 0;
} */