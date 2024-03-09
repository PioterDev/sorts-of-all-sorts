def insertionSort(l):
    for j in range(2, len(l)):
        key = l[j]
        i = j - 1
        while i > 0 and l[i] > key:
            l[i + 1] = l[i]
            i -= 1
        l[i + 1] = key