import sys
from rng import losowe, malejace, rosnace, a_ksztaltne, v_ksztaltne
from tester import isSorted, test

sys.setrecursionlimit(10**6)
        


'''
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
'''