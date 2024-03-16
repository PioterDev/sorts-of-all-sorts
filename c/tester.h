#ifndef TESTER_H
#define TESTER_H

/**
 * @brief 
 * 
 * @param algorithm (char) 'm' - merge sort, 'h' - heap sort, 's' - shell sort, 'r' - recursive quick sort, 'i' - iterative quick sort
 * @param testArr 
 * @param size size of testArr
 * @param printStuff set it to 0 to not print stuff in stdout
 * @return long long 
 */
long long test(char algorithm, int* testArr, int size, char printStuff);


#endif