## Requirements

- put item to the cache
- get item from the cache
- the cache has ttl.

## Flow: put item to the cache

1. if the item is already exist in the cache, just update ttl.
2. if the item is not in the cache,
  a. check the capacity, if full, delete least recently used item from the cache.
  b. add item to the cache.

## Flow: get item from the cache

1. if the key is not found in the cache, return None.
2. if the key is found
     a. check ttl, if it's expired, delete the item from the cache, return None.
     b. if the ttl is not expired, update ttl and return the item.

## Overview.

### Naive way.

Use a hash map for the cache.

- get: O(1)
- put: O(N) for the worst case, when we need to search a item to be deleted.

And O(N) for the space.

### Optimize put operation.

We need to know the oldest item in the hash at O(1) computing complexity.

We can use linked list. We can skip deleting item when get, just keep still keep it while the capacity is ok.

In that case, we need to add O(n) additional memory for the doubly linked list, and we hold the head & tail of that. We can use the hash key for the node value.

When, we add item, still O(1) because adding to the hashmap, and adding to the head of the linked list is both O(1), deleting also O(1).

### For thread safety

Based on the test cases, but if we want to use from the multi threaded environment, we need to use a lock for read & write operations.


```
class CacheItem(dataclass): // Any python object if it uses in a single threaded, else in multi-threaded, the item should be pickleable.
   ...

class CacheNode:
  key: string
  prev: None | CacheNode
  next: None | CacheNode

class LRUCache:
  def __init__(self):
     self._cache = {} // Hashmap
     self._head = None
     self._tail = None
     self._capacity = N
     self._ttl = L

  @property
  def size(self) -> int: // O(N)
    return len(list(self._cache.keys()))

  def _is_cache_full(self) -> boolean:
    return self.size == self._capacity

  def _hash(self, item: any) -> int:
    return hash(item)

  def put(self, item: any):
    if item is None:
      return // Or we can raise an exception.
    key = self._hash(item)
    if key in self._cache:
      return

    // We need to delete old one.
    if self._is_cache_full():
      tail = self._tail
      if tail is not None:
        self._tail = tail.prev
        self._tail.next = None

    self._cache[key] = item
    current_head = self._head
    current_head.prev = node
    node = CacheNode(key, None, current_head)
    current_head.prev = node
    self._head = node

  def get(self, key: string) -> None | Item:
    if not isinstance(key, string):
      raise ValueError('Invalid key type.')
    return self._cache.get(key)
```
