import sys
from rng import losowe, malejace, rosnace, a_ksztaltne, v_ksztaltne
from tester import isSorted, test

sys.setrecursionlimit(10**6)

def main():
    mode = input("W jaki tryb ma przejść program? (0 dla prezentowania, 1 dla testowania) [0/1]: ")
    match mode:
         case 0:
            mainPresenting()
         case 1:
            mainTesting()

def mainTesting():
    '''
    
    '''
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

    timings = {
        "losowe": {
            "shell": [],
            "merge": [],
            "heap": [],
            "quick-recursive": [],
            "quick-iterative": []
        },
        "rosnace": {
            "shell": [],
            "merge": [],
            "heap": [],
            "quick-recursive": [],
            "quick-iterative": []
        },
        "malejace": {
            "shell": [],
            "merge": [],
            "heap": [],
            "quick-recursive": [],
            "quick-iterative": []
        },
        "a_ksztaltne": {
            "shell": [],
            "merge": [],
            "heap": [],
            "quick-recursive": [],
            "quick-iterative": []
        },
        "v_ksztaltne": {
            "shell": [],
            "merge": [],
            "heap": [],
            "quick-recursive": [],
            "quick-iterative": []
        }
    }

    n = 64
    for i in range(10):
        print(f"Iteracja nr {i+1}\nDługość zadana: {n}")
        print("Generowanie ciągu losowego...")
        arrLosowe =     losowe(n)
        print("Generowanie ciągu rosnącego...")
        arrRosnace =    rosnace(n)
        print("Generowanie ciągu malejącego...")
        arrMalejace =   malejace(n)
        print("Generowanie ciągu A-kształtnego...")
        arrAKsztaltne = a_ksztaltne(n)
        print("Generowanie ciągu V-kształtnego...")
        arrVKsztaltne = v_ksztaltne(n)
        arr = [arrLosowe, arrRosnace, arrMalejace, arrAKsztaltne, arrVKsztaltne]
        for j in range(5): #arr ma stałe len
            #Shell Sort z algorytmem bazowym Insertion Sort oraz przyrostami Hibbarda,
            #Merge Sort,
            #Heap Sort,
            #Quick Sort rekurencyjny z pivotem, którym jest skrajnie prawy element ciągu,
            #Quick Sort iteracyjny z pivotem, którym jest skrajnie prawy element ciągu.
            shell = test("shell",               arr[j])
            merge = test("merge",               arr[j])
            heap = test("heap",                 arr[j])
            quickR = test("quick-recursive",    arr[j])
            quickI = test("quick-iterative",    arr[j])
            wyniki = [shell, merge, heap, quickR, quickI]
            if j == 0:
                timings["losowe"]       ["shell"]          .append(wyniki[0])
                timings["losowe"]       ["merge"]          .append(wyniki[1])
                timings["losowe"]       ["heap"]           .append(wyniki[2])
                timings["losowe"]       ["quick-recursive"].append(wyniki[3])
                timings["losowe"]       ["quick-iterative"].append(wyniki[4])
            elif j == 1:
                timings["rosnace"]      ["shell"]          .append(wyniki[0])
                timings["rosnace"]      ["merge"]          .append(wyniki[1])
                timings["rosnace"]      ["heap"]           .append(wyniki[2])
                timings["rosnace"]      ["quick-recursive"].append(wyniki[3])
                timings["rosnace"]      ["quick-iterative"].append(wyniki[4])
            elif j == 2:
                timings["malejace"]     ["shell"]          .append(wyniki[0])
                timings["malejace"]     ["merge"]          .append(wyniki[1])
                timings["malejace"]     ["heap"]           .append(wyniki[2])
                timings["malejace"]     ["quick-recursive"].append(wyniki[3])
                timings["malejace"]     ["quick-iterative"].append(wyniki[4])
            elif j == 3:
                timings["a_ksztaltne"]  ["shell"]          .append(wyniki[0])
                timings["a_ksztaltne"]  ["merge"]          .append(wyniki[1])
                timings["a_ksztaltne"]  ["heap"]           .append(wyniki[2])
                timings["a_ksztaltne"]  ["quick-recursive"].append(wyniki[3])
                timings["a_ksztaltne"]  ["quick-iterative"].append(wyniki[4])
            elif j == 4:
                timings["v_ksztaltne"]  ["shell"]          .append(wyniki[0])
                timings["v_ksztaltne"]  ["merge"]          .append(wyniki[1])
                timings["v_ksztaltne"]  ["heap"]           .append(wyniki[2])
                timings["v_ksztaltne"]  ["quick-recursive"].append(wyniki[3])
                timings["v_ksztaltne"]  ["quick-iterative"].append(wyniki[4])
            else: continue
        n *= 2

def mainPresenting():
    pass 
    #TODO: dokończyć
     
#main()