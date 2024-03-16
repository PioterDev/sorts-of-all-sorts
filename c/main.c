#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <windows.h>

#include "additional.h"
#include "heapsort.h"
#include "mergesort.h"
#include "quicksort.h"
#include "rng.h"
#include "shellsort.h"
#include "tester.h"

#define DO_PRINT 0      //<----- These things control whether to print out additional information during testing, 
#define DO_PRINT_TYPE 0 //<----- not really recommended if the program is bound to run for several hours.

int main(int argc, char** argv) {
    printf("Welcome to a sorting algorithm tester!\n");
    FILE* wyniki = fopen("./dane.csv", "a");
    if(wyniki == NULL){
        printf("Error with the file 'data.csv'\n");
        return 1;
    }
    printf("Everything okay with the file...for now :)\n");

    LARGE_INTEGER frequency;
    QueryPerformanceFrequency(&frequency);
    fseek(wyniki, 0, SEEK_END);
    long size = ftell(wyniki);
    printf("%ld\n", size);
    if(size == 0)fprintf(wyniki, "#Czas bazowy (przez ile nalezy podzielic liczby w pliku aby otrzymac czas w sekundach): %d\n", frequency.QuadPart);
    
    int n = 114000;
    while(n <= 1000000) {
        printf("Wielkosc zadana: %d\n", n);
        for(int i = 0; i < 10; i++) {
            printf("Iteracja nr %d\n", i+1);
            //losowe
            if(DO_PRINT_TYPE)printf("Typ danych: losowe\n");
            int* testArrLosowe = losowe(n);
            fprintf(wyniki, "%d, Losowe, ", n);
            fprintf(wyniki, "%lld, ", test('h', testArrLosowe, n, DO_PRINT));
            fprintf(wyniki, "%lld, ", test('m', testArrLosowe, n, DO_PRINT));
            fprintf(wyniki, "%lld, ", test('r', testArrLosowe, n, DO_PRINT));
            fprintf(wyniki, "%lld, ", test('i', testArrLosowe, n, DO_PRINT));
            fprintf(wyniki, "%lld\n", test('s', testArrLosowe, n, DO_PRINT));
            free(testArrLosowe);
            //rosnace
            if(DO_PRINT_TYPE)printf("Typ danych: rosnace\n");
            int* testArrRosnace = rosnace(n);
            fprintf(wyniki, "%d, Rosnace, ", n);
            fprintf(wyniki, "%lld, ", test('h', testArrRosnace, n, DO_PRINT));
            fprintf(wyniki, "%lld, ", test('m', testArrRosnace, n, DO_PRINT));
            fprintf(wyniki, "%lld, ", test('r', testArrRosnace, n, DO_PRINT));
            fprintf(wyniki, "%lld, ", test('i', testArrRosnace, n, DO_PRINT));
            fprintf(wyniki, "%lld\n", test('s', testArrRosnace, n, DO_PRINT));
            free(testArrRosnace);
            //malejace
            if(DO_PRINT_TYPE)printf("Typ danych: malejace\n");
            int* testArrMalejace = malejace(n);
            fprintf(wyniki, "%d, Malejace, ", n);
            fprintf(wyniki, "%lld, ", test('h', testArrMalejace, n, DO_PRINT));
            fprintf(wyniki, "%lld, ", test('m', testArrMalejace, n, DO_PRINT));
            fprintf(wyniki, "%lld, ", test('r', testArrMalejace, n, DO_PRINT));
            fprintf(wyniki, "%lld, ", test('i', testArrMalejace, n, DO_PRINT));
            fprintf(wyniki, "%lld\n", test('s', testArrMalejace, n, DO_PRINT));
            free(testArrMalejace);
            //v-ksztaltne
            if(DO_PRINT_TYPE)printf("Typ danych: V-ksztaltne\n");
            int* testArrV = v_ksztaltne(n);
            fprintf(wyniki, "%d, V-ksztaltne, ", n);
            fprintf(wyniki, "%lld, ", test('h', testArrV, n, DO_PRINT));
            fprintf(wyniki, "%lld, ", test('m', testArrV, n, DO_PRINT));
            fprintf(wyniki, "%lld, ", test('r', testArrV, n, DO_PRINT));
            fprintf(wyniki, "%lld, ", test('i', testArrV, n, DO_PRINT));
            fprintf(wyniki, "%lld\n", test('s', testArrV, n, DO_PRINT));
            free(testArrV);
            //a-ksztaltne
            if(DO_PRINT_TYPE)printf("Typ danych: A-ksztaltne\n");
            int* testArrA = a_ksztaltne(n);
            fprintf(wyniki, "%d, A-ksztaltne, ", n);
            fprintf(wyniki, "%lld, ", test('h', testArrA, n, DO_PRINT));
            fprintf(wyniki, "%lld, ", test('m', testArrA, n, DO_PRINT));
            fprintf(wyniki, "%lld, ", test('r', testArrA, n, DO_PRINT));
            fprintf(wyniki, "%lld, ", test('i', testArrA, n, DO_PRINT));
            fprintf(wyniki, "%lld\n", test('s', testArrA, n, DO_PRINT));
            free(testArrA);
        }

        n += 1000;
    }
    fclose(wyniki);
    return 0;
}
