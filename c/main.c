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

#define DO_PRINT 0
#define DO_PRINT_TYPE 0

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
        /*
        Wygeneruj po 10 n-elementowych ciągów zawierających liczby naturalne 
        losowe, rosnące, malejące, A-kształtne i V-kształtne, 
        dla 10-15 różnych wartości n. 

        Przykład ciągu A-kształtnego: 1,3,5,7,8,6,4,2. 
        Przykład ciągu V-kształtnego: 8,6,4,2,1,3,5,7,9.

        Liczby w każdym ciągu należą do przedziału <1,10*n>. 
        Przedział dla n należy dobrać eksperymentalnie - ciągi powinny być wystarczająco długie, 
        aby można było zaobserwować jak rośnie 
        czas obliczeń w zależności od n, a jednocześnie by 
        możliwe było wykonanie pomiarów.

        Przykładowo: generujemy 10 losowych ciągów 
        po 1000 elementów z przedziału <1,10000>, 
        sortujemy je algorytmem A i wyznaczamy 
        średni czas jaki algorytm ten potrzebuje aby posortować 
        losowy ciąg 1000-elementowy - to będzie jeden punkt na wykresie; 
        następnie generujemy 10 losowych ciągów po 5000 elementów z przedziału <1,50000>
        i sortujemy je algorytmem A, liczymy średni czas - to będzie drugi punkt na wykresie; 
        tę procedurę wykonujemy dla 10 różnych n.
        */
        printf("Wielkosc zadana: %d\n", n);
        for(int i = 0; i < 10; i++) {
            printf("Iteracja nr %d\n", i+1);
            //losowe
            /* if(DO_PRINT_TYPE)printf("Typ danych: losowe\n");
            int* testArrLosowe = losowe(n);
            fprintf(wyniki, "%d, Losowe, ", n);
            fprintf(wyniki, "%lld, ", test('h', testArrLosowe, n, DO_PRINT));
            fprintf(wyniki, "%lld, ", test('m', testArrLosowe, n, DO_PRINT));
            fprintf(wyniki, "%lld, ", test('r', testArrLosowe, n, DO_PRINT));
            fprintf(wyniki, "%lld, ", test('i', testArrLosowe, n, DO_PRINT));
            fprintf(wyniki, "%lld\n", test('s', testArrLosowe, n, DO_PRINT));
            free(testArrLosowe); */
            //rosnace
            if(DO_PRINT_TYPE)printf("Typ danych: rosnace\n");
            int* testArrRosnace = rosnace(n);
            fprintf(wyniki, "%d, Rosnace, ", n);
            fprintf(wyniki, "%lld, ", test('h', testArrRosnace, n, DO_PRINT));
            fprintf(wyniki, "%lld, ", test('m', testArrRosnace, n, DO_PRINT));
            //fprintf(wyniki, "%lld, ", test('r', testArrRosnace, n, DO_PRINT));
            //fprintf(wyniki, "%lld, ", test('i', testArrRosnace, n, DO_PRINT));
            fprintf(wyniki, "%lld\n", test('s', testArrRosnace, n, DO_PRINT));
            free(testArrRosnace);
            //malejace
            if(DO_PRINT_TYPE)printf("Typ danych: malejace\n");
            int* testArrMalejace = malejace(n);
            fprintf(wyniki, "%d, Malejace, ", n);
            fprintf(wyniki, "%lld, ", test('h', testArrMalejace, n, DO_PRINT));
            fprintf(wyniki, "%lld, ", test('m', testArrMalejace, n, DO_PRINT));
            //fprintf(wyniki, "%lld, ", test('r', testArrMalejace, n, DO_PRINT));
            //fprintf(wyniki, "%lld, ", test('i', testArrMalejace, n, DO_PRINT));
            fprintf(wyniki, "%lld\n", test('s', testArrMalejace, n, DO_PRINT));
            free(testArrMalejace);
            //v-ksztaltne
            if(DO_PRINT_TYPE)printf("Typ danych: V-ksztaltne\n");
            int* testArrV = v_ksztaltne(n);
            fprintf(wyniki, "%d, V-ksztaltne, ", n);
            fprintf(wyniki, "%lld, ", test('h', testArrV, n, DO_PRINT));
            fprintf(wyniki, "%lld, ", test('m', testArrV, n, DO_PRINT));
            //fprintf(wyniki, "%lld, ", test('r', testArrV, n, DO_PRINT));
            //fprintf(wyniki, "%lld, ", test('i', testArrV, n, DO_PRINT));
            fprintf(wyniki, "%lld\n", test('s', testArrV, n, DO_PRINT));
            free(testArrV);
            //a-ksztaltne
            if(DO_PRINT_TYPE)printf("Typ danych: A-ksztaltne\n");
            int* testArrA = a_ksztaltne(n);
            fprintf(wyniki, "%d, A-ksztaltne, ", n);
            fprintf(wyniki, "%lld, ", test('h', testArrA, n, DO_PRINT));
            fprintf(wyniki, "%lld, ", test('m', testArrA, n, DO_PRINT));
            //fprintf(wyniki, "%lld, ", test('r', testArrA, n, DO_PRINT));
            //fprintf(wyniki, "%lld, ", test('i', testArrA, n, DO_PRINT));
            fprintf(wyniki, "%lld\n", test('s', testArrA, n, DO_PRINT));
            free(testArrA);
        }

        n += 1000;
    }
    return 0;
}
