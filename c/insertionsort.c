#include <stdlib.h>

void insertionSort(int arr[], int n, int start, int step) {
    if(step < 1)step = 1;
    for(int i = start + step; i < n; i += step) {
        int key = arr[i], j = i - step;
        while(j >= start && arr[j] > key) {
            arr[j + step] = arr[j];
            j -= step;
        }
        arr[j + step] = key;
    }
}

/* int* insertionSortWithReturn(int arr[], int n) {
    int* copied = (int*) malloc(sizeof(int) * n);
    for(int i = 0; i < n; i++) {
        copied[i] = arr[i];
    }
    for(int i = 1; i < n; i++) {
        int key = copied[i], j = i - 1;
        while(j >= 0 && copied[j] > key) {
            copied[j + 1] = copied[j];
            j--;
        }
        copied[j + 1] = key;
    }
    return copied;
} */