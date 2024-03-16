#ifndef QUICKSORT_H
#define QUICKSORT_H


/**
 * @brief Recursive quick sort.
 * 
 * @param arr pointer to array 
 * @param p starting index
 * @param r ending index (if you want to sort the whole array, r = length - 1)
 * @param reverse whether to sort in reverse, any value other than 0 will cause sorting in reverse
 */
void quickSort(int* arr, int p, int r, int reverse);

void quickSortIterative(int* arr, int p, int r, int reverse);


#endif