# Code Review: LRU Cache with TTL Implementation

**Reviewer**: Claude
**Date**: 2025-11-28
**Status**: Planning Phase - Issues Found

## Summary

The plan demonstrates a solid understanding of LRU cache fundamentals and the optimization from O(N) to O(1) using a doubly-linked list. However, there are several critical implementation issues that need to be addressed before proceeding to code.

## Critical Issues

### 1. TTL Not Implemented ⚠️ **BLOCKER**

**Location**: PLAN.md:48-49, 74-98

**Issue**: While TTL is mentioned in requirements, it's never actually implemented:
- `CacheItem` is declared but not fully defined with expiry tracking
- No timestamp/expiry field in cache items
- `put()` doesn't set expiration time
- `get()` returns the item without checking if it's expired

**Expected**:
```python
class CacheItem:
    value: any
    expiry_time: float  # Unix timestamp when item expires

# In put():
item = CacheItem(value, time.time() + self._ttl)

# In get():
if time.time() > item.expiry_time:
    # Delete and return None
```

**Impact**: The cache won't enforce TTL at all.

---

### 2. put() Violates Requirements ⚠️ **BLOCKER**

**Location**: PLAN.md:78-79

**Issue**:
```python
if key in self._cache:
    return  # Just returns without updating TTL
```

**Requirement #1 states**: "if the item is already exist in the cache, just update ttl."

**Expected**: Update the expiry time and move to head of LRU list.

**Impact**: Items won't have their TTL refreshed on re-insertion.

---

### 3. Cache Dictionary Not Cleaned on Eviction ⚠️ **BLOCKER**

**Location**: PLAN.md:82-86

**Issue**:
```python
if self._is_cache_full():
    tail = self._tail
    if tail is not None:
        self._tail = tail.prev
        self._tail.next = None
    # Missing: del self._cache[tail.key]
```

**Impact**: Memory leak - evicted items remain in the dictionary, breaking capacity limits.

---

### 4. Null Pointer Risk ⚠️ **HIGH**

**Location**: PLAN.md:86

**Issue**:
```python
self._tail = tail.prev
self._tail.next = None  # If tail.prev is None, this will crash
```

**Impact**: Runtime error when evicting the last item in a single-item cache.

**Fix**: Add null check before accessing `self._tail.next`.

---

### 5. Node Creation Order Bug ⚠️ **BLOCKER**

**Location**: PLAN.md:88-93

**Issue**:
```python
current_head = self._head
current_head.prev = node  # 'node' doesn't exist yet!
node = CacheNode(key, None, current_head)  # Created after being used
current_head.prev = node  # Redundant
```

**Impact**: NameError - `node` referenced before assignment.

**Fix**: Create node before using it.

---

### 6. get() Doesn't Update LRU Order ⚠️ **BLOCKER**

**Location**: PLAN.md:95-98

**Issue**:
```python
def get(self, key: string) -> None | Item:
    return self._cache.get(key)
```

This implementation:
- Doesn't check if item is expired
- Doesn't move accessed item to head (update LRU order)
- Doesn't update TTL as mentioned in requirements

**Expected**:
1. Check if key exists
2. Check if expired → delete and return None
3. Move node to head of linked list
4. Update TTL
5. Return value

**Impact**: The cache becomes a simple hash map, losing both LRU and TTL functionality.

---

### 7. Data Structure Mismatch ⚠️ **HIGH**

**Location**: PLAN.md:88

**Issue**: Your cache maps `key -> item`, but to achieve O(1) node updates, you need `key -> CacheNode`.

**Current**: `self._cache[key] = item`
**Should be**: `self._cache[key] = node`

**Why**: When accessing an item in `get()`, you need to move that specific node to the head. If you only store the item, you can't find its node in O(1).

**Impact**: Can't efficiently update LRU order without scanning the entire linked list.

---

## Minor Issues

### 8. Incorrect Complexity Comment

**Location**: PLAN.md:65

**Issue**: Comment says `// O(N)` but `len()` on Python dict is O(1).

---

### 9. Unnecessary Hash Function

**Location**: PLAN.md:71-72

**Issue**: The `_hash()` method is unnecessary - Python dicts already handle hashing internally.

**Suggestion**: Remove it and use keys directly.

---

### 10. Missing Edge Cases

**Not covered in plan**:
- Empty cache initialization (`_head` and `_tail` both None)
- First item insertion when cache is empty
- Thread safety mentioned but not implemented

---

## Suggested Data Structure

```python
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
        self._capacity = capacity
        self._ttl = ttl_seconds
```

---

## Recommendations

1. **Implement TTL tracking** - Add expiry_time to CacheItem
2. **Fix put() logic** - Update TTL when key exists, clean up evicted items from dict
3. **Fix get() logic** - Check expiry, move to head, update LRU order
4. **Change data structure** - Map keys to nodes, not items
5. **Handle edge cases** - Empty cache, single item, null checks
6. **Add tests** - Cover all flows including expiry, eviction, and edge cases

---

## Positive Aspects ✅

- Correct identification of optimization path (naive O(N) → doubly-linked list O(1))
- Good understanding of space/time complexity tradeoffs
- Clear documentation of requirements and flows
- Consideration of thread safety needs

---

## Next Steps

1. Address all blocker issues before implementation
2. Update PLAN.md with corrected pseudo-code
3. Implement actual code with proper error handling
4. Write comprehensive test cases
5. Consider whether thread safety is needed for your use case
