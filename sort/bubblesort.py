def bubbleSort(l, reverse=False):
    for i in range(len(l)):
        for j in range(len(l)):
            if reverse:
                if l[i] < l[j]:
                    l[i], l[j] = l[j], l[i]
            else:
                if l[i] > l[j]:
                    l[i], l[j] = l[j], l[i]

