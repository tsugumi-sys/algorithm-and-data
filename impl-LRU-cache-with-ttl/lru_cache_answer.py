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

        # Dummy head/tail nodes to avoid edge checks when moving nodes.
        self.head = CacheNode("__head__", CacheItem(None, float("inf")))
        self.tail = CacheNode("__tail__", CacheItem(None, float("inf")))
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_to_front(self, node: CacheNode):
        node.prev = self.head
        node.next = self.head.next
        if node.next:
            node.next.prev = node
        self.head.next = node

    def _remove_node(self, node: CacheNode):
        prev_node = node.prev
        next_node = node.next
        if prev_node:
            prev_node.next = next_node
        if next_node:
            next_node.prev = prev_node
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
        lru = self.tail.prev
        if lru and lru is not self.head:
            self._remove_node(lru)
            del self.cache[lru.key]

    def _ensure_capacity(self):
        while len(self.cache) >= self.capacity and self.capacity > 0:
            lru = self.tail.prev
            if not lru or lru is self.head:
                break
            if self._is_expired(lru):
                self._remove_node(lru)
                del self.cache[lru.key]
                continue
            self._evict_lru()
            break

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
