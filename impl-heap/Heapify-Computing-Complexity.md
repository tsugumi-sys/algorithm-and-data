# Why `_heapify()` Runs in **O(n)**

*(GitHub-compatible, no LaTeX)*

This explanation uses one consistent definition of height, chosen so the math and intuition align perfectly.

---

# 1. Height Definition (Consistent)

We define height `h` as the number of levels **above the bottom**:

```
h = 0  → bottom level (leaves)
h = 1  → one level above leaves
h = 2  → two levels above leaves
...
h = H  → root (H ≈ log2(n))
```

This definition is ideal for `_heapify()` because:

* A node can move down at most `h` levels.
* Leaves (h=0) never move.
* The root (h=H) can move the farthest.

---

# 2. Number of Nodes at Height `h`

A binary heap is a **complete binary tree**.

In such a tree:

* The bottom level contains about `n/2` nodes.
* The level above contains about `n/4` nodes.
* Then `n/8`, etc.

So the number of nodes at height `h` is approximately:

```
nodes(h) ≈ n / 2^(h+1)
```

Example:

```
h = 0 → ~ n/2 nodes
h = 1 → ~ n/4 nodes
h = 2 → ~ n/8 nodes
...
h = H → 1 node (the root)
```

This pattern is the backbone of the heapify complexity analysis.

---

# 3. Cost per Node at Height `h`

A node at height `h` may need to sift down **at most h levels**.

So:

```
cost_per_node(h) = h
```

Examples:

* Leaves (h = 0) → cost 0
* Nodes one level above leaves (h = 1) → cost 1
* Root (h = H) → max cost H

This height definition matches sift-down behavior exactly.

---

# 4. Total Cost of `_heapify()`

Total work = sum of (nodes at height h) × (cost per node).

```
T(n) ≈ sum over h=0..H of:  (n / 2^(h+1)) * h
```

Factor out `n`:

```
T(n) ≈ n * sum over h=0..∞ of (h / 2^(h+1))
```

Now, there is a classical identity:

```
sum over h=1..∞ of (h / 2^h) = 2
```

Therefore:

```
T(n) ≈ n * (1/2) * 2 = n
```

So heapify runs in:

```
O(n)
```

---

# 5. Intuition (No Math Needed)

* About **n/2** nodes are leaves → cost 0
* About **n/4** nodes may move 1 level
* About **n/8** nodes may move 2 levels
* About **n/16** nodes may move 3 levels
* ...

Each level has fewer nodes, but higher possible cost.
The two factors cancel out, and the total stays proportional to `n`.

This is why bottom-up heap construction beats calling `push()` `n` times (which would be `O(n log n)`).

---

# 6. Final Summary

* Height `h` is counted from the bottom (leaves = 0).
* Nodes at height `h` ≈ `n / 2^(h+1)`.
* Cost per node at height `h` = `h`.
* Total work is proportional to `n`.

```
Bottom-up heap construction runs in O(n) time.
```
