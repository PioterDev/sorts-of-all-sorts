import math
from .insertionsort import insertionSortWithReturn

def hibbard(k: int):
    return 2 ** k - 1

#this function is for determining the first Hibbard's number index to use
#to limit initial insertion sort to <= 32 elements in my case
def hibbard_inverse(y: int):
    return math.log2(y + 1)

def shellSort(l, reverse=False, printCurrentNum=False): #this Shell sort uses Hibbard's numbers as values for increments
    length = len(l) 
    #I'll make it so that the 1st sorting takes <= 32 elements
    k = math.floor(hibbard_inverse(length)) - 4
    if k < 0: k = 2
    H = hibbard(k)
    while H >= 1:
        if printCurrentNum:
            print(f"Current Hibbard's number: {H}")
        for i in range(H):
            l[i::H] = insertionSortWithReturn(l[i::H], reverse)
        k -= 1
        H = hibbard(k)
    