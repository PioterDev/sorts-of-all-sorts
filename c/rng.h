#ifndef RNG_H
#define RNG_H

/**
 * @brief Generates a random integer from range <0, 2⁶⁴ - 1>.
 * 
 * @return unsigned long long 
 */
unsigned long long randomUll();

/**
 * @brief Generates an ACTUAL random integer from range <0, 2³² - 1>.
 * 
 * @return unsigned int 
 */
unsigned int random();

/**
 * @brief Returns an array of size n of random unsigned long longs.
 * 
 * @param n 
 * @return unsigned long long*
 */
unsigned long long* rngUll(int n);

/**
 * @brief Returns an array of size n of random integers.
 * 
 * @param n 
 * @param lowerBound
 * @param upperBound
 * @return int* 
 */
int* rngInt(int n, int lowerBound, int upperBound);

int* losowe(int n);
int* rosnace(int n);
int* malejace(int n);
int* v_ksztaltne(int n);
int* a_ksztaltne(int n);


#endif