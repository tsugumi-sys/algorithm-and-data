Interface

    class LinkedList:
        append(value): add a node to the tail of the list
        prepend(value): add a node to the head of the list
        insert(index, value): insert at a zero-based position (len is allowed, otherwise raise IndexError)
        pop_first(): remove and return the head value (raise IndexError if empty)
        pop_last(): remove and return the tail value (raise IndexError if empty)
        find(value): return True if any node stores the value
        __len__(): return the number of nodes
        __iter__(): yield values from head to tail so list(linked_list) works

Implement everything in `main.py`. Feel free to add helper classes (like `Node`) if you want. No need for anything fancy—just get the basics working so the tests in `test.py` pass.
