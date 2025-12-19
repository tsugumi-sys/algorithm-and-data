class MinHeap:
    def __init__(self, values=None):
        self._heap = [] if values is None else list(values)
        if self._heap:
            try:
                self._heapify()
            except TypeError as exc:
                raise TypeError("Heap items must be mutually comparable") from exc

    def _heapify(self):
        for idx in range((len(self._heap) - 2) // 2, -1, -1):
            self._sift_down(idx)

    def _sift_down(self, idx):
        n = len(self._heap)
        while True:
            left = 2 * idx + 1
            right = left + 1
            smallest = idx
            if left < n and self._heap[left] < self._heap[smallest]:
                smallest = left
            if right < n and self._heap[right] < self._heap[smallest]:
                smallest = right
            if smallest == idx:
                break
            self._heap[idx], self._heap[smallest] = (
                self._heap[smallest],
                self._heap[idx],
            )
            idx = smallest

    def _bubble_up(self, idx):
        while idx > 0:
            parent = (idx - 1) // 2
            if self._heap[idx] < self._heap[parent]:
                self._heap[idx], self._heap[parent] = (
                    self._heap[parent],
                    self._heap[idx],
                )
                idx = parent
            else:
                break

    def _ensure_comparable(self, value):
        if not self._heap:
            return
        try:
            _ = value < self._heap[0]
            _ = self._heap[0] < value
        except TypeError as exc:
            raise TypeError("Heap items must be mutually comparable") from exc

    def push(self, value):
        self._ensure_comparable(value)
        self._heap.append(value)
        self._bubble_up(len(self._heap) - 1)

    def pop(self):
        if self.is_empty():
            raise IndexError("Heap is empty")
        self._heap[0], self._heap[-1] = self._heap[-1], self._heap[0]
        value = self._heap.pop()
        if self._heap:
            self._sift_down(0)
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Heap is empty")
        return self._heap[0]

    def __len__(self):
        return len(self._heap)

    def is_empty(self):
        return len(self._heap) == 0


class MaxHeap:
    def __init__(self, values=None):
        self._heap = [] if values is None else list(values)
        if self._heap:
            try:
                self._heapify()
            except TypeError as exc:
                raise TypeError("Heap items must be mutually comparable") from exc

    def _heapify(self):
        for idx in range((len(self._heap) - 2) // 2, -1, -1):
            self._sift_down(idx)

    def _sift_down(self, idx):
        n = len(self._heap)
        while True:
            left = 2 * idx + 1
            right = left + 1
            largest = idx
            if left < n and self._heap[left] > self._heap[largest]:
                largest = left
            if right < n and self._heap[right] > self._heap[largest]:
                largest = right
            if largest == idx:
                break
            self._heap[idx], self._heap[largest] = self._heap[largest], self._heap[idx]
            idx = largest

    def _bubble_up(self, idx):
        while idx > 0:
            parent = (idx - 1) // 2
            if self._heap[idx] > self._heap[parent]:
                self._heap[idx], self._heap[parent] = (
                    self._heap[parent],
                    self._heap[idx],
                )
                idx = parent
            else:
                break

    def _ensure_comparable(self, value):
        if not self._heap:
            return
        try:
            _ = value > self._heap[0]
            _ = self._heap[0] > value
        except TypeError as exc:
            raise TypeError("Heap items must be mutually comparable") from exc

    def push(self, value):
        self._ensure_comparable(value)
        self._heap.append(value)
        self._bubble_up(len(self._heap) - 1)

    def pop(self):
        if self.is_empty():
            raise IndexError("Heap is empty")
        self._heap[0], self._heap[-1] = self._heap[-1], self._heap[0]
        value = self._heap.pop()
        if self._heap:
            self._sift_down(0)
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Heap is empty")
        return self._heap[0]

    def __len__(self):
        return len(self._heap)

    def is_empty(self):
        return len(self._heap) == 0
