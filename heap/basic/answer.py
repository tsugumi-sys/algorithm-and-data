class MinHeap:
    def __init__(self, values=None):
        """Create a min-heap from optional initial values (heapified in-place)."""
        self._heap = [] if values is None else list(values)
        if self._heap:
            try:
                self._heapify()
            except TypeError as exc:
                raise TypeError("Heap items must be mutually comparable") from exc

    def _heapify(self):
        """
        Bottom-up heapify to enforce the heap property in O(n).

        Starts at the last parent index ( (n-2)//2 ) and sifts each node down,
        skipping leaves because they already satisfy the heap property.

        Please check ./Heapify-Computing-Complexity.md for more details.
        """
        for idx in range((len(self._heap) - 2) // 2, -1, -1):
            self._sift_down(idx)

    def _sift_down(self, idx):
        """
        Restore order by pushing the item at idx down to its correct spot.
        Picks the smaller child (for min-heap) to swap with until both children
        are >= current. Example:
          heap = [3, 4, 1] at idx=0 -> swap with child 1 -> [1, 4, 3].
        """
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
        """Restore order by bubbling the item at idx up toward the root."""
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
        """Fail fast if the new value cannot be compared with existing items."""
        if not self._heap:
            return
        try:
            _ = value < self._heap[0]
            _ = self._heap[0] < value
        except TypeError as exc:
            raise TypeError("Heap items must be mutually comparable") from exc

    def push(self, value):
        """Insert a value and restore the heap by bubbling up."""
        self._ensure_comparable(value)
        self._heap.append(value)
        self._bubble_up(len(self._heap) - 1)

    def pop(self):
        """Remove and return the smallest item; raise if empty."""
        if self.is_empty():
            raise IndexError("Heap is empty")
        self._heap[0], self._heap[-1] = self._heap[-1], self._heap[0]
        value = self._heap.pop()
        if self._heap:
            self._sift_down(0)
        return value

    def peek(self):
        """Return the smallest item without removing it; raise if empty."""
        if self.is_empty():
            raise IndexError("Heap is empty")
        return self._heap[0]

    def __len__(self):
        """Return number of items in the heap."""
        return len(self._heap)

    def is_empty(self):
        """Return True when the heap has no items."""
        return len(self._heap) == 0


class MaxHeap:
    def __init__(self, values=None):
        """Create a max-heap from optional initial values (heapified in-place)."""
        self._heap = [] if values is None else list(values)
        if self._heap:
            try:
                self._heapify()
            except TypeError as exc:
                raise TypeError("Heap items must be mutually comparable") from exc

    def _heapify(self):
        """
        Bottom-up heapify to enforce the heap property in O(n).
        Starts at the last parent index ( (n-2)//2 ) and sifts each node down,
        skipping leaves because they already satisfy the heap property.
        Example: n=8 => start at index 3; iterate 3,2,1,0.
        """
        for idx in range((len(self._heap) - 2) // 2, -1, -1):
            self._sift_down(idx)

    def _sift_down(self, idx):
        """
        Restore order by pushing the item at idx down to its correct spot.
        Picks the larger child (for max-heap) to swap with until both children
        are <= current. Example:
          heap = [2, 4, 1] at idx=0 -> swap with child 4 -> [4, 2, 1].
        """
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
        """Restore order by bubbling the item at idx up toward the root."""
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
        """Fail fast if the new value cannot be compared with existing items."""
        if not self._heap:
            return
        try:
            _ = value > self._heap[0]
            _ = self._heap[0] > value
        except TypeError as exc:
            raise TypeError("Heap items must be mutually comparable") from exc

    def push(self, value):
        """Insert a value and restore the heap by bubbling up."""
        self._ensure_comparable(value)
        self._heap.append(value)
        self._bubble_up(len(self._heap) - 1)

    def pop(self):
        """Remove and return the largest item; raise if empty."""
        if self.is_empty():
            raise IndexError("Heap is empty")
        self._heap[0], self._heap[-1] = self._heap[-1], self._heap[0]
        value = self._heap.pop()
        if self._heap:
            self._sift_down(0)
        return value

    def peek(self):
        """Return the largest item without removing it; raise if empty."""
        if self.is_empty():
            raise IndexError("Heap is empty")
        return self._heap[0]

    def __len__(self):
        """Return number of items in the heap."""
        return len(self._heap)

    def is_empty(self):
        """Return True when the heap has no items."""
        return len(self._heap) == 0
