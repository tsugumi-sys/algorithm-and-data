Interface

    class MinHeap:
        __init__(values=None): optionally start the heap with an iterable of values
        push(value): add a value to the heap
        pop(): remove and return the smallest value (raise IndexError if empty)
        peek(): return the smallest value without removing it (raise IndexError if empty)
        __len__(): return the number of stored values
        is_empty(): return True when the heap has no values

    class MaxHeap:
        __init__(values=None): optionally start the heap with an iterable of values
        push(value): add a value to the heap
        pop(): remove and return the largest value (raise IndexError if empty)
        peek(): return the largest value without removing it (raise IndexError if empty)
        __len__(): return the number of stored values
        is_empty(): return True when the heap has no values

Use a binary heap (array-based) implementation. Duplicates are allowed and should be returned the correct number of times.
Implement everything in `main.py`.
