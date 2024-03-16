#include <stdio.h>
#include "additional.h"

void heapify(int arr[], int n, int i) {
    //Previous implementation (this one) is bad, removing it
    /* for(int i = n/2; i > 0; i--) {
        int parent = arr[i - 1];
        int left = arr[2 * i - 1];
        if(isInitial){
            if(left > parent)swap(&arr[i-1], &arr[2*i-1]);
            continue;
        }
        int right = arr[2 * i];
        if(left > parent && right > parent) {
            if(left > right)swap(&arr[2*i-1], &arr[i-1]);
            else swap(&arr[2*i], &arr[i-1]);
        }
        else if(left > parent)swap(&arr[2*i-1], &arr[i-1]);
        else if(right > parent)swap(&arr[2*i], &arr[i-1]);
        else continue;
    } */
    int largest = i, left = 2*i + 1, right = 2*i + 2;
    if(left < n && arr[i] < arr[left])largest = left;
    if(right < n && arr[largest] < arr[right])largest = right;
    if(largest != i) {
        swap(&arr[i], &arr[largest]);
        heapify(arr, n, largest);
    }
}

void heapSort(int arr[], int n) {
    heapify(arr, n, 1);
    for(int i = n / 2; i > -1; i--)heapify(arr, n, i);
    for(int i = n - 1; i > 0; i--){
        swap(&arr[0], &arr[i]);
        heapify(arr, i, 0);
    }
}


/* int main() {
    int test[11] = {3, 1, 6, 10, 9, 8, 4, 5, 8, 2, 12};
    int length = sizeof(test) / sizeof(test[0]);
    printArray(test, length);
    heapSort(test, length);
    printArray(test, length);
    return 0;
} */