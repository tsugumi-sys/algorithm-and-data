class MinHeap:
    def __init__(self, values=None):
        # https://docs.python.org/3.13/faq/programming.html#how-do-i-convert-between-tuples-and-lists
        # If the argument is a list, it makes a copy just like seq[:] would.
        # NOTE: For this problem, we restrict values as int or float for simplicity.
        #   In the actual situation, heap should be generalized for any data types and comparable.
        if values is None:
            self._heap = []
        else:
            if not all(isinstance(v, int) for v in values):
                raise TypeError("All elements must be int")
            self._heap = list(
                values
            )  # create an copy to avoid modifying the given value directly.

    def push(self, value):
        raise NotImplementedError

    def pop(self):
        raise NotImplementedError

    def peek(self):
        raise NotImplementedError

    def __len__(self):
        raise NotImplementedError

    def is_empty(self):
        raise NotImplementedError


class MaxHeap:
    def __init__(self, values=None):
        raise NotImplementedError

    def push(self, value):
        raise NotImplementedError

    def pop(self):
        raise NotImplementedError

    def peek(self):
        raise NotImplementedError

    def __len__(self):
        raise NotImplementedError

    def is_empty(self):
        raise NotImplementedError
