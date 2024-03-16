@echo off
cls
gcc -o main main.c additional.c heapsort.c mergesort.c quicksort.c rng.c shellsort.c tester.c insertionsort.c -Wl,--stack,1073741824