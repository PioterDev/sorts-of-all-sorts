class Stack: # a helper class for the iterative version
    maxSize = 0
    currentIndex = -1
    stack = []
    def __init__(self, maxSize: int) -> None:
        self.stack = [0] * maxSize
        self.maxSize = maxSize
        self.currentIndex = -1
    def push(self, el):
        self.currentIndex += 1
        self.stack[self.currentIndex] = el
        return self
    def pop(self):
        self.currentIndex -= 1
        return self.stack[self.currentIndex + 1]
    def __str__(self) -> str:
        return f"Max stack size: {self.maxSize}\nCurrent index: {self.currentIndex}\nElements: {self.stack}"
      
def quickSortRecursive(l, p, r):
    if p < r:
        q = partition(l, p, r)
        quickSortRecursive(l, p, q - 1)
        quickSortRecursive(l, q + 1, r)
#Ah, the recursive version is so clean, yet risking a stack overflow... I love it

def partition(l, p, r):
    pivot = l[r]
    i = p - 1
    for j in range(p, r):
        if l[j] < pivot:
            i += 1
            l[i], l[j] = l[j], l[i]
    l[i+1], l[r] = l[r], l[i+1]
    return i+1

def quickSortIterative(l, p, r): 
    size = r - p + 1 #len(l) also works, but why would you use it?
    stack = Stack(size)
    stack.push(p)
    stack.push(r)
    while stack.currentIndex >= 0:
        r = stack.pop()
        p = stack.pop()
        q = partition(l, p, r) 
        if q - 1 > p: 
            stack.push(p)
            stack.push(q - 1)
        if q + 1 < r: 
            stack.push(q + 1)
            stack.push(r)