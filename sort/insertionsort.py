def insertionSort(l, reverse=False):
    if reverse:
        for i in range(1, len(l)):
            key = l[i]
            j = i - 1
            while j >= 0 and l[j] < key:
                l[j + 1] = l[j]
                j -= 1
            l[j + 1] = key
    else:
        for i in range(1, len(l)):
            key = l[i]
            j = i - 1
            while j >= 0 and l[j] > key:
                l[j + 1] = l[j]
                j -= 1
            l[j + 1] = key
        
def insertionSortWithReturn(l, reverse=False):
    if reverse:
        for i in range(1, len(l)):
            key = l[i]
            j = i - 1
            while j >= 0 and l[j] < key:
                l[j + 1] = l[j]
                j -= 1
            l[j + 1] = key
    else:
        for i in range(1, len(l)):
            key = l[i]
            j = i - 1
            while j >= 0 and l[j] > key:
                l[j + 1] = l[j]
                j -= 1
            l[j + 1] = key
    return l