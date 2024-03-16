# Sorting algorithms
If you're looking for a C implementation, go to the "C" directory. The rest is written in Python.

## How they work
A few keywords.

Sorting in-place - it means the algorithm doesn't require copying the elements somewhere, excluding of course the program stack and CPU registers.

Stability - if the algorithm is stable, it will preserve the initial order of identical elements.

Let's say we have [3, 1, 1, 5, 6, 0] as input. In a stable algorithm, the 2nd "1" will not be placed before the 1st "1". For numbers it doesn't really matter, but sorting more complex data sets may require it.

Big O notation - it is used to describe a range of functions that will limit the function in question from the top.

It is not strict, meaning for example, f(x) = x<sup>2</sup> is O(n<sup>2</sup>), but it technically also is O(n<sup>3</sup>), O(n<sup>4</sup>) and so on, but we usually use the lowest one, so in this case - O(n<sup>2</sup>).
### Heap sort
Heap sort is based on the principles of a heap, a.k.a - a binary tree, where the root is the largest/smallest element.

It works by continously extracting the largest/smallest element by heapifying the array, swapping the root with the last index, decrementing the last index and re-heapifying the array.

It sorts in-place, but isn't stable.

Average case time complexity - O(n log n)

Best case time complexity - O(n log n)

Worst case time complexity - O(n log n)

### Merge sort
Simply put, divide-and-conquer.

It works by recursively splitting the array in half until it's no longer possible and merging it in a correct order.

It doesn't sort in-place, but it's stable.

Average case time complexity - O(n log n)

Best case time complexity - O(n log n)

Worst case time complexity - O(n log n)

### Quick sort
Similar to merge sort, but works on a different principle.

It works by partitioning the array based on a chosen "pivot" - a value somewhere in the array - it moves elements smaller than pivot to its left and larger ones to the right.

There are 2 approaches to quick sort:
- recursive - afer partitioning, recursively sorts 2 sub-arrays - one with starting index 0 and ending index q - the index of a pivot after partitioning, and the other with starting index q+1 and ending index being the last index.
- iterative - it's a bit more difficult to describe, it's better to look at the code.

It is one of the fastest sorting algorithms if the pivot chosen is optimal, otherwise its performance is terrible.

It sorts in place, but isn't stable.

Average case time complexity - O(n log n)

Best case time complexity - O(n log n)

Worst case time complexity - O(n<sup>2</sup>)

### Shell sort
Shell sort operates under some other sorting algorithm and some chosen increments.

It works by sorting sub-arrays that are a given increment apart from each other with a chosen base algorithm and lowering the increment.

It sorts in-place, but isn't stable.

Its time complexity is dependent on the chosen base algorithm and increments.
