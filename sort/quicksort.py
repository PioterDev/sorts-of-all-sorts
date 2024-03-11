from additional import Stack

def quickSortRecursive(l: list[int], p: int, r: int, reverse=False):
    if p < r:
        q = partition(l, p, r, reverse)
        quickSortRecursive(l, p, q - 1, reverse)
        quickSortRecursive(l, q + 1, r, reverse)
#Ah, the recursive version is so clean, yet risking a stack overflow... I love it

def partition(l: list[int], p: int, r: int, reverse=False):
    pivot = l[r]
    i = p - 1
    for j in range(p, r):
        if reverse:
            if l[j] > pivot:
                i += 1
                l[i], l[j] = l[j], l[i]
        else:
            if l[j] < pivot:
                i += 1
                l[i], l[j] = l[j], l[i]
    l[i+1], l[r] = l[r], l[i+1]
    return i+1

def quickSortIterative(l: list[int], p: int, r: int, reverse=False): 
    size = r - p + 1 #len(l) also works, but why would you use it?
    stack = Stack(size)
    stack.push(p)
    stack.push(r)
    while stack.currentIndex >= 0:
        r = stack.pop()
        p = stack.pop()
        q = partition(l, p, r, reverse) 
        if q - 1 > p: 
            stack.push(p)
            stack.push(q - 1)
        if q + 1 < r: 
            stack.push(q + 1)
            stack.push(r)