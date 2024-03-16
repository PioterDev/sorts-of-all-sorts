#include <stdio.h>
#include <time.h>
#include <stdlib.h>

#include "quicksort.h"

unsigned long long randomUll() {
    return (unsigned long long)rand() << 32 | (unsigned long)rand();
}

unsigned int random() {
    return (unsigned int)rand() << 16 | rand();
}

unsigned long long* rngUll(int n) {
    unsigned long long* arr = malloc(sizeof(long long) * n);
    srand(time(NULL));
    for(int i = 0; i < n; i++) {
        arr[i] = randomUll() % n;
    }
    return arr;
}

int* rngInt(int n, int lowerBound, int upperBound) {
    int* arr = (int*) malloc(sizeof(int) * n);
    srand(time(NULL));
    for(int i = 0; i < n; i++) {
        arr[i] = (int) random() % upperBound + lowerBound;
    }
    return arr;
}

int* losowe(int n) {
    return rngInt(n, 1, 10*n);
}

int* rosnace(int n) {
    int* arr = rngInt(n, 1, 10*n);
    quickSort(arr, 0, n - 1, 0);
    return arr;
}

int* malejace(int n) {
    int* arr = rngInt(n, 1, 10*n);
    quickSort(arr, 0, n - 1, 1);
    return arr;
}

int* v_ksztaltne(int n) {
    int middle = n / 2;
    int* arr = rngInt(n, 1, 10*n);
    quickSort(arr, 0, middle, 1);
    quickSort(arr, middle + 1, n - 1, 0);
    return arr;
}

int* a_ksztaltne(int n) {
    int middle = n / 2;
    int* arr = rngInt(n, 1, 10*n);
    quickSort(arr, 0, middle, 0);
    quickSort(arr, middle + 1, n - 1, 1);
    return arr;
}

/* int main(char* args) {

    FILE* numbers = fopen("./numbers.txt", "a");
    int n;
    printf("Podaj dlugosc: ");
    scanf("%d", &n);
    unsigned long long* r = rng(n);
    fprintf(numbers, "%d\n", n);
    for(int i = 0; i <= n-2; i++) {
        fprintf(numbers, "%llu\n", r[i]);
    }
    fprintf(numbers, "%llu", r[n-1]);
    fclose(numbers);
    return 0;

} */
/* int main() {
    int* test = v_ksztaltne(100);
    for(int i = 0; i < 100; i++) {
        printf("%d ", test[i]);
    }
} */