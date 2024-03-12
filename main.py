import sys, math, os
from rng import losowe, malejace, rosnace, a_ksztaltne, v_ksztaltne
from tester import isSorted, test

sys.setrecursionlimit(10**6)

def main():
    print("sorts-of-all-sorts v1.0")    
    print("Wpisanie w dowolnym miejscu 'q' zakończy program.")
    print("Natomiast wpisanie 'b' powróci do poprzedniego menu.")
    mode = input("W jaki tryb ma przejść program? (p dla prezentowania, t dla testowania, q dla wyjścia): ")
    match mode:
        case "p":
            os.system("cls")
            mainPresenting()
        #case "t":
        #    mainTesting()
        case "q": exit()

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
            key = ""
            if j == 0:
                key = "losowe"
            elif j == 1:
                key = "rosnace"
            elif j == 2:
                key = "malejace"
            elif j == 3:
                key = "a_ksztaltne"
            elif j == 4:
                key = "v_ksztaltne"
            else:
                print("What? Huh?? How is that even possible???")
                continue
            timings[key]       ["shell"]          .append(wyniki[0])
            timings[key]       ["merge"]          .append(wyniki[1])
            timings[key]       ["heap"]           .append(wyniki[2])
            timings[key]       ["quick-recursive"].append(wyniki[3])
            timings[key]       ["quick-iterative"].append(wyniki[4])
        n *= 2

def mainPresenting():
    print("sorts-of-all-sorts v1.0, tryb: prezentacja")    
    print("Wpisanie w dowolnym miejscu 'q' zakończy program.")
    print("Natomiast wpisanie 'b' powróci do poprzedniego menu.")
    while True:
        print("\nWybierz co chcesz zrobić.")
        print("Dla wczytania ciągu z klawiatury, wpisz 'k'")
        print("Dla wygenerowania ciągu za pomocą generatora, wpisz 'g'")
        print("Dla wyjścia, wpisz 'q'")
        print("Wpisanie w dowolnym miejscu 'q' zakończy program.")
        print("Natomiast wpisanie 'b' powróci do poprzedniego menu.")
        option = input("Wybrana opcja: ")
        match option:
            case "q": exit()
            case "k":
                while True:
                    l = input("\nWypisz liczby rozdzielone spacją: ")
                    if l == "b": break
                    elif l == "q": exit()
                    else: l = [int(x) for x in l.split()]
                    print("\nWybierz algorytm sortujący.")
                    print("Dla Shell sorta, wpisz 's'")
                    print("Dla Merge sorta, wpisz 'm'")
                    print("Dla Heap sorta, wpisz 'h'")
                    print("Dla Quick sorta w wersji rekurencyjnej, wpisz 'qr'")
                    print("Dla Quick sorta w wersji iteracyjnej, wpisz 'qi'")
                    algorithm = input("Wybrana opcja: ")
                    if algorithm == "q": exit()
                    elif algorithm == "b": break
                    reverse = input("\nCzy chcesz sortować wstecz? [y/n]: ")
                    if reverse == "q": exit()
                    elif reverse == "b": break
                    elif reverse == "y": reverse = True
                    elif reverse == "n": reverse = False
                    else:
                        print("Zakładam w takim razie, że nie.")
                        reverse = False
                    algo = ""
                    match algorithm:
                        case "s":
                            algo = "Wybrany algorytm: Shell sort"
                        case "m":
                            algo = "Wybrany algorytm: Merge sort"
                        case "h":
                            algo = "Wybrany algorytm: Heap sort"
                        case "qr":
                            algo = "Wybrany algorytm: Rekurencyjny quick sort"
                        case "qi":
                            algo = "Wybrany algorytm: Iteracyjny quick sort"
                        case "q": exit()
                        case "b": break
                        case _:
                            print("Niepoprawna opcja, spróbuj ponownie.\n")
                            break
                    print(f"Zadany ciąg: {l}")
                    print(algo)
                    t = 0
                    match algorithm:
                        case "s":
                            t = test("shell", l, "pl", reverse, printTime=False)
                        case "m":
                            t = test("merge", l, "pl", reverse, printTime=False)
                        case "h":
                            t = test("heap", l, "pl", reverse, printTime=False)
                        case "qr":
                            t = test("quick-recursive", l, "pl", reverse, printTime=False)
                        case "qi":
                            t = test("quick-iterative", l, "pl", reverse, printTime=False)
                    print(f"Czas potrzebny do posortowania: {t} ns")
            case "g":
                while True:
                    n = input("\nJakiej długości ciąg chcesz wygenerować? ")
                    if n == "q": exit()
                    elif n == "b": break
                    else: n = int(n)
                    if math.isnan(n):
                        print("Niepoprawna długość, spróbuj ponownie.\n")
                    print("Jakiego typu ciąg chcesz wygenerować?")
                    print("Dla losowego, wpisz 'l'")
                    print("Dla rosnącego, wpisz 'r'")
                    print("Dla malejącego, wpisz 'm'")
                    print("Dla A-kształtnego, wpisz 'A'")
                    print("Dla V-kształtnego, wpisz 'V'")
                    arrType = input("Wybrana opcja: ")
                    if arrType == "q": exit()
                    elif arrType == "b": break
                    print("\nWybierz algorytm sortujący.")
                    print("Dla Shell sorta, wpisz 's'")
                    print("Dla Merge sorta, wpisz 'm'")
                    print("Dla Heap sorta, wpisz 'h'")
                    print("Dla Quick sorta w wersji rekurencyjnej, wpisz 'qr'")
                    print("Dla Quick sorta w wersji iteracyjnej, wpisz 'qi'")
                    algorithm = input("Wybrana opcja: ")
                    if algorithm == "q": exit()
                    elif algorithm == "b": break
                    reverse = input("\nCzy chcesz sortować wstecz? [y/n]: ")
                    if reverse == "q": exit()
                    elif reverse == "b": break
                    elif reverse == "y": reverse = True
                    elif reverse == "n": reverse = False
                    else:
                        print("Zakładam w takim razie, że nie.")
                        reverse = False
                    typeArr = ""
                    match arrType:
                        case "l":
                            typeArr = "Wybrany typ ciągu: losowy"
                        case "r":
                            typeArr = "Wybrany typ ciągu: rosnący"
                        case "m":
                            typeArr = "Wybrany typ ciągu: malejący"
                        case "A":
                            typeArr = "Wybrany typ ciągu: A-kształtny"
                        case "V":
                            typeArr = "Wybrany typ ciągu: V-kształtny"
                        case "q": exit()
                        case "b": break
                        case _:
                            print("Niepoprawna opcja, spróbuj ponownie.\n")
                            break
                    print(typeArr)
                    algo = ""
                    match algorithm:
                        case "s":
                            algo = "Wybrany algorytm: Shell sort"
                        case "m":
                            algo = "Wybrany algorytm: Merge sort"
                        case "h":
                            algo = "Wybrany algorytm: Heap sort"
                        case "qr":
                            algo = "Wybrany algorytm: Rekurencyjny quick sort"
                        case "qi":
                            algo = "Wybrany algorytm: Iteracyjny quick sort"
                        case "q": exit()
                        case "b": break
                        case _:
                            print("Niepoprawna opcja, spróbuj ponownie.\n")
                            break
                    print(algo)
                    match arrType:
                        case "l":
                            arr = losowe(n)
                            match algorithm:
                                case "s":
                                    test("shell", arr, "pl", reverse)
                                case "m":
                                    test("merge", arr, "pl", reverse)
                                case "h":
                                    test("heap", arr, "pl", reverse)
                                case "qr":
                                    test("quick-recursive", arr, "pl", reverse)
                                case "qi":
                                    test("quick-iterative", arr, "pl", reverse)
                                case "q": exit()
                        case "r":
                            arr = rosnace(n)
                            match algorithm:
                                case "s":
                                    test("shell", arr, "pl", reverse)
                                case "m":
                                    test("merge", arr, "pl", reverse)
                                case "h":
                                    test("heap", arr, "pl", reverse)
                                case "qr":
                                    test("quick-recursive", arr, "pl", reverse)
                                case "qi":
                                    test("quick-iterative", arr, "pl", reverse)
                                case "q": exit()
                        case "m":
                            arr = malejace(n)
                            match algorithm:
                                case "s":
                                    test("shell", arr, "pl", reverse)
                                case "m":
                                    test("merge", arr, "pl", reverse)
                                case "h":
                                    test("heap", arr, "pl", reverse)
                                case "qr":
                                    test("quick-recursive", arr, "pl", reverse)
                                case "qi":
                                    test("quick-iterative", arr, "pl", reverse)
                                case "q": exit()  
                        case "A":
                            arr = a_ksztaltne(n)
                            match algorithm:
                                case "s":
                                    test("shell", arr, "pl", reverse)
                                case "m":
                                    test("merge", arr, "pl", reverse)
                                case "h":
                                    test("heap", arr, "pl", reverse)
                                case "qr":
                                    test("quick-recursive", arr, "pl", reverse)
                                case "qi":
                                    test("quick-iterative", arr, "pl", reverse)
                                case "q": exit() 
                        case "V":
                            arr = v_ksztaltne(n)
                            match algorithm:
                                case "s":
                                    test("shell", arr, "pl", reverse)
                                case "m":
                                    test("merge", arr, "pl", reverse)
                                case "h":
                                    test("heap", arr, "pl", reverse)
                                case "qr":
                                    test("quick-recursive", arr, "pl", reverse)
                                case "qi":
                                    test("quick-iterative", arr, "pl", reverse)
                                case "q": exit()
                        case "q": exit()
                    print("Koniec testu.\n")
                    continue
            case _:
                print("Nieznana opcja, powrót do głównego menu")
                continue     
    #TODO: dokończyć
     
main()