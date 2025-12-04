import time
from dataclasses import dataclass
from typing import Any


@dataclass
class CacheItem:
    value: Any
    expiry_time: float


class CacheNode:
    def __init__(self, key: Any, item: CacheItem):
        self.key = key
        self.item = item
        self.prev: CacheNode | None = None
        self.next: CacheNode | None = None


class LRUCache:
    def __init__(self, capacity: int, ttl_seconds: float):
        if capacity < 0:
            raise ValueError("Capacity cannot be negative")
        if ttl_seconds < 0:
            raise ValueError("TTL cannot be negative")

        self.capacity = capacity
        self.ttl_seconds = ttl_seconds
        self.cache: dict[Any, CacheNode] = {}
        self.head: CacheNode | None = None
        self.tail: CacheNode | None = None

    def _add_to_front(self, node: CacheNode):
        if not self.head:
            # List is empty
            self.head = self.tail = node
            node.prev = node.next = None
        else:
            # Add to front
            node.prev = None
            node.next = self.head
            self.head.prev = node
            self.head = node

    def _remove_node(self, node: CacheNode):
        if node.prev:
            node.prev.next = node.next
        else:
            # Removing head
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            # Removing tail
            self.tail = node.prev

        node.prev = None
        node.next = None

    def _move_to_front(self, node: CacheNode):
        self._remove_node(node)
        self._add_to_front(node)

    def _is_expired(self, node: CacheNode) -> bool:
        return time.time() >= node.item.expiry_time

    def _refresh_expiry(self, node: CacheNode):
        node.item.expiry_time = time.time() + self.ttl_seconds

    def _evict_lru(self):
        if self.tail:
            lru = self.tail
            self._remove_node(lru)
            del self.cache[lru.key]

    def _ensure_capacity(self):
        # First, remove all expired items from the tail
        while self.tail and self._is_expired(self.tail):
            lru = self.tail
            self._remove_node(lru)
            del self.cache[lru.key]

        # Then, if still at capacity, evict one non-expired LRU item
        if len(self.cache) >= self.capacity and self.capacity > 0:
            self._evict_lru()

    def get(self, key: Any) -> Any:
        node = self.cache.get(key)
        if not node:
            return None

        if self._is_expired(node):
            self._remove_node(node)
            del self.cache[key]
            return None

        self._refresh_expiry(node)
        self._move_to_front(node)
        return node.item.value

    def put(self, key: Any, item: Any):
        existing = self.cache.get(key)
        if existing:
            if self._is_expired(existing):
                self._remove_node(existing)
                del self.cache[key]
            else:
                existing.item.value = item
                self._refresh_expiry(existing)
                self._move_to_front(existing)
                return

        if self.capacity == 0:
            return

        self._ensure_capacity()

        expiry_time = time.time() + self.ttl_seconds
        node = CacheNode(key, CacheItem(item, expiry_time))
        self.cache[key] = node
        self._add_to_front(node)

    @property
    def size(self) -> int:
        return len(self.cache)
