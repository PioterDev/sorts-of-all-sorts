#include <stdio.h>
#include <stdlib.h>

void swap(int* x, int* y) {
    int tmp = *x;
    *x = *y;
    *y = tmp;
}

void printArray(int arr[], int n) {
    for(int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

void bin(unsigned int n) {
    unsigned int i;
    for (i = 1 << 31; i > 0; i = i / 2)
        (n & i) ? printf("1") : printf("0");
    printf("\n");
}

int* copy(int* something, int size) {
    int* copied = malloc(sizeof(int) * size);
    for(int i = 0; i < size; i++) {
        copied[i] = something[i];
    }
    return copied;
}

int isSorted(int arr[], int n) {
    for(int i = 1; i < n; i++) {
        if(arr[i] < arr[i - 1])return -1;
    }
    return 0;
}