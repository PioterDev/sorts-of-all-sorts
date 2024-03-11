import math

def heapSort(l, reverse=False):
    n = len(l)
    for i in range(n // 2, -1, -1):
        heapify(l, n, i, reverse)
    #heapify(l, len(l))
    for i in range(n - 1, 0, -1):
        l[i], l[0] = l[0], l[i]
        heapify(l, i, 0, reverse)

#THIS IMPLEMENTATION IS BAD, DON'T USE THIS   
def heapifyBad(l, length):
    for i in range(length // 2, 0, -1):
        Parent = l[i - 1]
        Left = l[2*i - 1]
        if length == len(l) and length%2 == 0: #when the last parent has only 1 child
            if Left > Parent:
                l[i - 1], l[2*i - 1] = l[2*i - 1], l[i - 1]
            else: continue
        else:
            Right = l[2*i]
            if Left > Parent and Right > Parent:
                if Left > Right:
                    l[i - 1], l[2*i - 1] = l[2*i - 1], l[i - 1]
                else:
                    l[i - 1], l[2*i] = l[2*i], l[i - 1]
            elif Left > Parent:
                l[i - 1], l[2*i - 1] = l[2*i - 1], l[i - 1]
            elif Right > Parent:
                l[i - 1], l[2*i] = l[2*i], l[i - 1]
            else: continue

def heapify(l, n, i, reverse=False):
    if reverse:
        smallest = i
        left = 2*i + 1
        right = 2*i + 2
        if left < n and l[i] > l[left]:
            smallest = left
        if right < n and l[smallest] > l[right]:
            smallest = right
        if smallest != i:
            l[i], l[smallest] = l[smallest], l[i]
            heapify(l, n, smallest, reverse)
    else:
        largest = i
        left = 2*i + 1
        right = 2*i + 2
        if left < n and l[i] < l[left]:
            largest = left
        if right < n and l[largest] < l[right]:
            largest = right
        if largest != i:
            l[i], l[largest] = l[largest], l[i]
            heapify(l, n, largest, reverse)

 
'''
test = [3, 1, 6, 10, 9, 8, 4, 5, 8, 2, 12]
print(test)
heapSort(test)
'''
