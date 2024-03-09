import math

calls = 0

def mergeSort(l, reverse=False):
    length = len(l)
    if length == 1:
        return l
    elif length > 1:
        middle = math.floor(length / 2)
        if reverse:
            return merge(mergeSort(l[middle:], reverse), mergeSort(l[:middle], reverse), reverse)
        return merge(mergeSort(l[:middle]), mergeSort(l[middle:]), reverse)        
        
def merge(left, right, reverse=False):
    global calls
    calls += 1
    i = j = 0
    merged = []
    #print(left, right)
    while i < len(left) and j < len(right):
        if reverse:
            if left[i] > right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        else:
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else: 
                merged.append(right[j])
                j += 1
    while i < len(left):
        merged.append(left[i])
        i += 1
    while j < len(right):
        merged.append(right[j])
        j += 1
    #print(merged, "\n")
    return merged

'''
l = []
rev = False
for i in range(25):
    l.append(random.randint(0, 99))
m = math.floor(len(l) / 2)
print("Original list: ", l)
print("Sorting in reverse: ", rev)
print("Sorted list: ", mergeSort(l, rev))
print("Calls: ", calls)
'''