#include <stdlib.h>

#include "rng.h"
#include "additional.h"

void merge(int arr[], int left, int middle, int right) { 
    int i, j, k; 
    int lenLeft = middle - left + 1; 
    int lenRight = right - middle; 
  
    int* Left = malloc(sizeof(int) * lenLeft);
    int* Right = malloc(sizeof(int) * lenRight);
    for (i = 0; i < lenLeft; i++)Left[i] = arr[left + i]; 
    for (j = 0; j < lenRight; j++)Right[j] = arr[middle + 1 + j]; 

    i = 0; 
    j = 0; 
  
    k = left; 
    while (i < lenLeft && j < lenRight) { 
        if (Left[i] < Right[j]) { 
            arr[k] = Left[i]; 
            i++; 
        } 
        else { 
            arr[k] = Right[j]; 
            j++; 
        } 
        k++; 
    } 
    while (i < lenLeft) { 
        arr[k] = Left[i]; 
        i++; 
        k++; 
    } 
    while (j < lenRight) { 
        arr[k] = Right[j]; 
        j++; 
        k++; 
    }
    free(Left);
    free(Right);
} 

void mergeSort(int arr[], int left, int right) { 
    if (left < right) { 
        int middle = left + (right - left) / 2; 

        mergeSort(arr, left, middle); 
        mergeSort(arr, middle + 1, right); 
  
        merge(arr, left, middle, right); 
    } 
}

/* int main() {
    int n = 100000000;
    int* arr = rngInt(n);
    FILE* unsortedFile = fopen("./unsorted.txt", "a");
    for(int i = 0; i < n - 1; i++) {
        fprintf(unsortedFile, "%d\n", arr[i]);
    }
    fprintf(unsortedFile, "%d", arr[n - 1]);
    fclose(unsortedFile);
    //printArray(arr, n);
    mergeSort(arr, 0, n - 1);
    //printArray(arr, n);
    printf("Sorted\n");
    FILE* sortedFile = fopen("./sorted.txt", "a");
    for(int i = 0; i < n - 1; i++) {
        fprintf(sortedFile, "%d\n", arr[i]);
    }
    fprintf(sortedFile, "%d", arr[n - 1]);
    fclose(sortedFile);
    return 0;
} */