import pytest
import time
from lru_cache_answer import LRUCache


# ============================================================================
# Basic Operations Tests
# ============================================================================


def test_put_and_get_single_item():
    cache = LRUCache(capacity=3, ttl_seconds=10)
    cache.put("key1", "value1")
    assert cache.get("key1") == "value1"


def test_get_nonexistent_key():
    cache = LRUCache(capacity=3, ttl_seconds=10)
    assert cache.get("nonexistent") is None


def test_put_multiple_items():
    cache = LRUCache(capacity=3, ttl_seconds=10)
    cache.put("key1", "value1")
    cache.put("key2", "value2")
    cache.put("key3", "value3")

    assert cache.get("key1") == "value1"
    assert cache.get("key2") == "value2"
    assert cache.get("key3") == "value3"


def test_update_existing_key():
    """When key exists, value should be updated and TTL refreshed"""
    cache = LRUCache(capacity=3, ttl_seconds=10)
    cache.put("key1", "value1")
    cache.put("key1", "value2")
    assert cache.get("key1") == "value2"


# ============================================================================
# LRU Eviction Tests
# ============================================================================


def test_evict_least_recently_used():
    cache = LRUCache(capacity=3, ttl_seconds=10)
    cache.put("key1", "value1")
    cache.put("key2", "value2")
    cache.put("key3", "value3")

    # Cache is full, adding key4 should evict key1 (least recently used)
    cache.put("key4", "value4")

    assert cache.get("key1") is None
    assert cache.get("key2") == "value2"
    assert cache.get("key3") == "value3"
    assert cache.get("key4") == "value4"


def test_evict_with_get_updates_lru_order():
    cache = LRUCache(capacity=3, ttl_seconds=10)
    cache.put("key1", "value1")
    cache.put("key2", "value2")
    cache.put("key3", "value3")

    # Access key1, making it most recently used
    cache.get("key1")

    # Add key4, should evict key2 (now least recently used)
    cache.put("key4", "value4")

    assert cache.get("key1") == "value1"
    assert cache.get("key2") is None
    assert cache.get("key3") == "value3"
    assert cache.get("key4") == "value4"


def test_evict_with_put_updates_lru_order():
    cache = LRUCache(capacity=3, ttl_seconds=10)
    cache.put("key1", "value1")
    cache.put("key2", "value2")
    cache.put("key3", "value3")

    # Update key1, making it most recently used
    cache.put("key1", "new_value1")

    # Add key4, should evict key2 (now least recently used)
    cache.put("key4", "value4")

    assert cache.get("key1") == "new_value1"
    assert cache.get("key2") is None
    assert cache.get("key3") == "value3"
    assert cache.get("key4") == "value4"


def test_single_item_cache():
    cache = LRUCache(capacity=1, ttl_seconds=10)
    cache.put("key1", "value1")
    assert cache.get("key1") == "value1"

    cache.put("key2", "value2")
    assert cache.get("key1") is None
    assert cache.get("key2") == "value2"


# ============================================================================
# TTL Expiration Tests
# ============================================================================


def test_item_expires_after_ttl():
    cache = LRUCache(capacity=3, ttl_seconds=0.1)
    cache.put("key1", "value1")

    # Item should be accessible immediately
    assert cache.get("key1") == "value1"

    # Wait for TTL to expire
    time.sleep(0.15)

    # Item should be expired and return None
    assert cache.get("key1") is None


def test_expired_item_is_removed_from_cache():
    """Expired items should be removed from cache, freeing up capacity"""
    cache = LRUCache(capacity=2, ttl_seconds=0.1)
    cache.put("key1", "value1")
    cache.put("key2", "value2")

    # Wait for items to expire
    time.sleep(0.15)

    # Access expired items (should trigger removal)
    cache.get("key1")
    cache.get("key2")

    # Should be able to add 2 new items without eviction
    cache.put("key3", "value3")
    cache.put("key4", "value4")

    assert cache.get("key3") == "value3"
    assert cache.get("key4") == "value4"


def test_get_refreshes_ttl():
    """Accessing an item should refresh its TTL"""
    cache = LRUCache(capacity=3, ttl_seconds=0.2)
    cache.put("key1", "value1")

    # Wait 0.15 seconds (not expired yet)
    time.sleep(0.15)

    # Access the item (should refresh TTL)
    assert cache.get("key1") == "value1"

    # Wait another 0.15 seconds
    time.sleep(0.15)

    # Item should still be valid (total 0.3s but TTL was refreshed at 0.15s)
    assert cache.get("key1") == "value1"


def test_put_existing_key_refreshes_ttl():
    """Re-inserting an existing key should refresh its TTL"""
    cache = LRUCache(capacity=3, ttl_seconds=0.2)
    cache.put("key1", "value1")

    # Wait 0.15 seconds
    time.sleep(0.15)

    # Update the item (should refresh TTL)
    cache.put("key1", "value1_updated")

    # Wait another 0.15 seconds
    time.sleep(0.15)

    # Item should still be valid
    assert cache.get("key1") == "value1_updated"


def test_different_items_expire_independently():
    cache = LRUCache(capacity=3, ttl_seconds=0.2)
    cache.put("key1", "value1")

    time.sleep(0.1)
    cache.put("key2", "value2")

    time.sleep(0.15)  # Total: 0.25s for key1, 0.15s for key2

    # key1 should be expired, key2 should still be valid
    assert cache.get("key1") is None
    assert cache.get("key2") == "value2"


# ============================================================================
# Edge Cases Tests
# ============================================================================


def test_empty_cache():
    cache = LRUCache(capacity=3, ttl_seconds=10)
    assert cache.get("any_key") is None


def test_capacity_zero():
    """Cache with zero capacity should not store anything"""
    cache = LRUCache(capacity=0, ttl_seconds=10)
    cache.put("key1", "value1")
    assert cache.get("key1") is None


def test_negative_capacity():
    """Should handle negative capacity gracefully"""
    with pytest.raises(ValueError):
        LRUCache(capacity=-1, ttl_seconds=10)


def test_zero_ttl():
    """Items with zero TTL should expire immediately"""
    cache = LRUCache(capacity=3, ttl_seconds=0)
    cache.put("key1", "value1")
    # Even immediate access might fail depending on timing
    # Just ensure it doesn't crash
    cache.get("key1")


def test_negative_ttl():
    """Should handle negative TTL gracefully"""
    with pytest.raises(ValueError):
        LRUCache(capacity=3, ttl_seconds=-1)


def test_put_none_value():
    """Should be able to store None as a value"""
    cache = LRUCache(capacity=3, ttl_seconds=10)
    cache.put("key1", None)
    assert cache.get("key1") is None
    # Note: This is ambiguous - need to decide if None means "not found" or "value is None"


def test_put_none_key():
    """Should handle None as a key (or raise error)"""
    cache = LRUCache(capacity=3, ttl_seconds=10)
    # This behavior depends on your design decision
    try:
        cache.put(None, "value1")
        assert cache.get(None) == "value1"
    except (ValueError, TypeError):
        pass  # Acceptable to reject None keys


def test_large_capacity():
    """Should handle large capacity values"""
    cache = LRUCache(capacity=10000, ttl_seconds=10)
    for i in range(100):
        cache.put(f"key{i}", f"value{i}")

    for i in range(100):
        assert cache.get(f"key{i}") == f"value{i}"


def test_complex_values():
    """Should handle various data types as values"""
    cache = LRUCache(capacity=5, ttl_seconds=10)

    cache.put("string", "value")
    cache.put("int", 42)
    cache.put("float", 3.14)
    cache.put("list", [1, 2, 3])
    cache.put("dict", {"a": 1, "b": 2})

    assert cache.get("string") == "value"
    assert cache.get("int") == 42
    assert cache.get("float") == 3.14
    assert cache.get("list") == [1, 2, 3]
    assert cache.get("dict") == {"a": 1, "b": 2}


# ============================================================================
# Cache Size Tests
# ============================================================================


def test_size_increases_on_put():
    cache = LRUCache(capacity=3, ttl_seconds=10)
    assert cache.size == 0

    cache.put("key1", "value1")
    assert cache.size == 1

    cache.put("key2", "value2")
    assert cache.size == 2


def test_size_does_not_exceed_capacity():
    cache = LRUCache(capacity=3, ttl_seconds=10)
    cache.put("key1", "value1")
    cache.put("key2", "value2")
    cache.put("key3", "value3")
    assert cache.size == 3

    cache.put("key4", "value4")
    assert cache.size == 3


def test_size_decreases_when_item_expires():
    cache = LRUCache(capacity=3, ttl_seconds=0.1)
    cache.put("key1", "value1")
    cache.put("key2", "value2")
    assert cache.size == 2

    time.sleep(0.15)

    # Access expired item to trigger removal
    cache.get("key1")

    # Size should decrease (implementation dependent)
    # This test assumes expired items are removed on access
    assert cache.size == 1


def test_size_unchanged_on_update():
    cache = LRUCache(capacity=3, ttl_seconds=10)
    cache.put("key1", "value1")
    cache.put("key2", "value2")
    assert cache.size == 2

    cache.put("key1", "updated_value1")
    assert cache.size == 2


# ============================================================================
# Concurrent Scenarios Tests
# ============================================================================


def test_alternating_get_and_put():
    cache = LRUCache(capacity=3, ttl_seconds=10)
    cache.put("key1", "value1")
    assert cache.get("key1") == "value1"

    cache.put("key2", "value2")
    assert cache.get("key1") == "value1"
    assert cache.get("key2") == "value2"

    cache.put("key3", "value3")
    assert cache.get("key2") == "value2"

    cache.put("key4", "value4")
    assert cache.get("key1") is None  # Evicted


def test_rapid_expiration_and_insertion():
    cache = LRUCache(capacity=2, ttl_seconds=0.05)

    cache.put("key1", "value1")
    cache.put("key2", "value2")

    time.sleep(0.06)

    # Both should be expired
    assert cache.get("key1") is None
    assert cache.get("key2") is None

    # Should be able to add new items
    cache.put("key3", "value3")
    cache.put("key4", "value4")

    assert cache.get("key3") == "value3"
    assert cache.get("key4") == "value4"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
