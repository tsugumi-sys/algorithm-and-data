Interface

    class DoublyLinkedList:
        append(value): add a node to the tail of the list
        prepend(value): add a node to the head of the list
        insert(index, value): insert at a zero-based position (raise IndexError for index < 0 or index > len; index == len appends)
        pop_first(): remove and return the head value (raise IndexError if empty)
        pop_last(): remove and return the tail value (raise IndexError if empty)
        find(value): return True if any node stores the value
        iter_reverse(): yield values from tail to head
        __len__(): return the number of nodes
        __iter__(): yield values from head to tail so list(doubly_linked_list) works

Implement everything in `main.py`. You can add a `Node` class with `prev` and `next` pointers if that helps. Keep it simple—just enough to satisfy the tests in `test.py`.
