import time
from dataclasses import dataclass


@dataclass
class CacheItem:
    value: any
    expiry_time: float


class CacheNode:
    def __init__(self, key: str, item: CacheItem):
        self.key = key
        self.item = item
        self.prev: CacheNode | None = None
        self.next: CacheNode | None = None


class LRUCache:
    def __init__(self, capacity: int, ttl_seconds: float):
        self._cache: dict[str, CacheNode] = {}  # key -> CacheNode
        self._head: CacheNode | None = None
        self._tail: CacheNode | None = None

        if capacity < 0:
            raise ValueError()
        self._capacity = capacity

        if ttl_seconds < 0:
            raise ValueError()
        self._ttl = ttl_seconds

    def get(self, key: str) -> any:
        """
        Retrieves a value from the cache and marks it as recently used.
        Returns None if key doesn't exist.
        """
        # If key doesn't exist, return None
        if key not in self._cache:
            return

        node = self._cache[key]

        # Check if the item is evicted.
        if node.item.expiry_time < time.time():
            # Delete the item.
            del self._cache[key]
            prev = node.prev
            next = node.next
            if prev is not None:
                prev.next = next
            else:
                # node was the head.
                self._head = None
            if next is not None:
                next.prev = prev
            else:
                self._tail = prev
            return None

        # Update the expiry time to current time + TTL (reset the TTL)
        node.item.expiry_time = time.time() + self._ttl

        # If already at head, no need to move
        if node.prev is None:
            return node.item.value

        # Step 1: Remove node from its current position
        prev = node.prev
        next = node.next  # possibly None if this is the tail

        # Link prev and next together
        prev.next = next

        if next is not None:
            # Node is in the middle, not at tail
            next.prev = prev
        else:
            # Node is at tail, update tail pointer to prev
            self._tail = prev

        # Step 2: Move node to the head
        current_head = self._head
        node.prev = None  # Node will be the new head, so no prev
        node.next = current_head

        if current_head is not None:
            current_head.prev = node

        self._head = node

        return node.item.value

    def put(self, key: str, item: any):
        """
        Adds or updates an item in the cache.
        If key exists: update value and TTL, move to head (most recently used).
        If capacity is full: evict the least recently used item (tail).
        New items are always added to the head.
        """
        if self._capacity == 0:
            return

        # If key already exists, update it and move to head
        if key in self._cache:
            node = self._cache[key]
            node.item.expiry_time = time.time() + self._ttl
            node.item.value = item

            # If already at head, nothing more to do
            if node.prev is None:
                return

            # Remove node from current position
            prev = node.prev
            next = node.next

            prev.next = next
            if next is not None:
                # Node is in the middle
                next.prev = prev
            else:
                # Node is at tail, update tail pointer
                self._tail = prev

            # Move to head
            current_head = self._head
            node.prev = None
            node.next = current_head
            current_head.prev = node
            self._head = node
            return

        # Key doesn't exist, create new node
        cache_item = CacheItem(value=item, expiry_time=time.time() + self._ttl)
        node = CacheNode(key, cache_item)

        # Case 1: Cache is empty - initialize both head and tail
        if len(self._cache.keys()) == 0:
            self._head = node
            self._tail = node
            self._cache[key] = node
            return

        # Case 2: Cache is at capacity - evict the tail (least recently used)
        if len(self._cache) == self._capacity:
            current_tail = self._tail
            # Remove from dictionary
            del self._cache[current_tail.key]

            # Update tail pointer
            prev_tail = current_tail.prev
            if prev_tail is not None:
                # There are other nodes besides the tail
                prev_tail.next = None
                self._tail = prev_tail
            else:
                # Only one node in cache, will be replaced completely
                # The new node will become both head and tail
                self._head = node
                self._tail = node
                self._cache[key] = node
                return

        # Case 3: Cache has space (or we just evicted) - add new node to head
        current_head = self._head
        node.prev = None  # New head has no prev
        node.next = current_head
        current_head.prev = node
        self._head = node

        self._cache[key] = node

    @property
    def size(self) -> int:
        return len(self._cache.keys())
