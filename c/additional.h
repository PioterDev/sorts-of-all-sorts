#ifndef ADDITIONAL_H
#define ADDITIONAL_H

/**
 * @brief Swaps. That's it.
 * 
 * @param x 
 * @param y 
 */
void swap(int* x, int* y);

/**
 * @brief Prints the given array.
 * 
 * @param arr array
 * @param n length of the array
 */
void printArray(int arr[], int n);

/**
 * @brief Prints the binary representation of a given unsigned integer.
 * 
 * @param n 
 */
void bin(unsigned int n);

int* copy(int* something, int size);


#endif