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

    def get(self, key: str) -> any:

    def put(self, key: str, item: any):

    @property
    def size(self) -> int:
        
