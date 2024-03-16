#include <stdio.h>
#include <stdlib.h>

#include "additional.h"

int partition(int* arr, int p, int r, int reverse) {
    int pivot = arr[r];
    int i  = p - 1;
    for(int j = p; j < r; j++){
        if(reverse) {
            if(arr[j] > pivot) {
                i++;
                swap(&arr[i], &arr[j]);
            }
        }
        else {
            if(arr[j] < pivot) {
                i++;
                swap(&arr[i], &arr[j]);
            }
        }
    }
    swap(&arr[i+1], &arr[r]);
    return i + 1;
}

void quickSort(int* arr, int p, int r, int reverse) {
    if(p < r) {
        int q = partition(arr, p, r, reverse);
        quickSort(arr, p, q-1, reverse);
        quickSort(arr, q+1, r, reverse);
    }
}

void quickSortIterative(int* arr, int p, int r, int reverse) {
    int size = r - p + 1;
    int* stack = malloc(sizeof(int) * size);
    int top = 0;

    stack[top] = p;
    top++;
    stack[top] = r;
    while(top >= 0) {
        r = stack[top];
        top--;
        p = stack[top];
        top--;
        int q = partition(arr, p, r, reverse);
        if(q - 1 > p){
            top++;
            stack[top] = p;
            top++;
            stack[top] = q - 1;
        }
        if(q + 1 < r) {
            top++;
            stack[top] = q + 1;
            top++;
            stack[top] = r;
        }
    }
}

/*int main() {
    FILE* fPtr;
    char path[256];
    printf("Podaj sciezke to pliku: ");
    scanf("%s", path);
    fPtr = fopen(path, "r");
    if(fPtr == NULL)printf("Error: no file\n");
    else printf("File found.\n");
    int size;
    fscanf(fPtr, "%d", &size);
    int* data = (int*) malloc(sizeof(int) * size);
    for(int i = 0; i <= size; i++) {
        fscanf(fPtr, "%d", &data[i]);
    }
    printf("Loaded array into memory.\n");
    fclose(fPtr);
    int data[10] = {5, 6, 1, 6, 2, 7, 8, 2, 10, 15};
    int length = sizeof(data) / sizeof(data[0]);
    //printArray(data, size);
    clock_t start = clock();
    quickSort(data, 0, size - 1);
    clock_t end = clock();
    double executionTime = (double) (end - start) / CLOCKS_PER_SEC;
    printf("Time spent sorting: %g\n", executionTime);
    FILE* numbersSorted = fopen("./numbersSorted.txt", "a");
    fprintf(numbersSorted, "%d\n", size);
    for(int i = 0; i <= size-2; i++) {
        fprintf(numbersSorted, "%d\n", data[i]);
    }
    fprintf(numbersSorted, "%d", data[size-1]);
    fclose(numbersSorted);
    //printArray(data, size);
    return 0;
}*/