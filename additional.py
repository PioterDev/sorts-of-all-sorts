class Stack: # a helper class for the iterative version of quick sort
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
    
