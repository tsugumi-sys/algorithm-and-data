# Why `_heapify()` Runs in **O(n)**

*(Consistent Top-Based Height Definition)*

This explanation uses a **top-based height measured from the bottom**, which is the only definition that keeps the analysis internally consistent.

---

# 1. Height Definition (Consistent)

We define height `h` as the distance **from the bottom level**:

```
h = 0 → bottom level (leaves)
h = 1 → one level above leaves
h = 2 → two levels above leaves
...
h = H → root (H = height of tree)
```

This definition is standard in tree theory:
**leaves have height 0, the root has the maximum height**.

This is the correct height model for heapify because:

* the maximum number of levels a node can move down = its height from the bottom
* leaves never move → cost = 0
* nodes near the root may move many levels → cost ≈ H

---

# 2. Number of Nodes at Height `h`

A binary heap is a **complete binary tree**, so:

* The bottom level contains about **n/2 nodes**.
* The next level contains about **n/4 nodes**.
* Then **n/8**, and so on.

Thus the number of nodes at height `h` is approximately:

[
\text{nodes}(h) \approx \frac{n}{2^{h+1}}
]

This is asymptotically accurate because each higher level contains half as many nodes as the one below it.

So we have:

```
h = 0 → ~ n/2 nodes
h = 1 → ~ n/4 nodes
h = 2 → ~ n/8 nodes
...
h = H → 1 node (the root)
```

This matches the structure of a complete binary tree perfectly.

---

# 3. Maximum Sift-Down Cost at Height `h`

A node at height `h` (distance from bottom) can move down **at most h levels**.

So the cost per node is:

[
\text{cost}(h) = h
]

Examples:

* Leaves (h = 0) never move.
* Their parents (h = 1) may move one level.
* Root (h = H) may move all the way down.

This height definition aligns naturally with sift-down behavior.

---

# 4. Total Cost of `_heapify()`

Total work is:

[
T(n)
= \sum_{h=0}^{H}
\big( \text{nodes}(h) \times \text{cost}(h) \big)
]

Substitute the approximations:

[
\text{nodes}(h) \approx \frac{n}{2^{h+1}}
\quad\text{and}\quad
\text{cost}(h) = h
]

Thus:

[
T(n)
\approx \sum_{h=0}^{H}
\left(\frac{n}{2^{h+1}} \cdot h\right)
]

Factor out `n`:

[
T(n)
\approx n \sum_{h=0}^{\infty}
\frac{h}{2^{h+1}}
]

---

# 5. Convergence of the Series

The series:

[
\sum_{h=1}^{\infty} \frac{h}{2^h}
]

is a known convergent series:

[
\sum_{h=1}^{\infty} \frac{h}{2^h} = 2
]

Therefore:

[
T(n)
= n \cdot \frac{1}{2} \cdot 2
= n
]

So:

[
\boxed{T(n) = O(n)}
]

---

# 6. Intuition

* Most nodes (~n/2) are leaves and require **zero** work.
* The next quarter (~n/4) may move **one step**.
* The next eighth (~n/8) may move **two steps**.
* Very few nodes are expensive to fix.
* The sum of all this work converges to a constant multiple of `n`.

Thus bottom-up heap construction is linear time.

---

# 7. Final Summary

> Using a consistent top-based height (measured from the bottom),
> level `h` contains about `n / 2^(h+1)` nodes, each costing at most `h` to sift down.
> The resulting series converges, giving the linear-time bound:
>
> [
> \boxed{T(n) = O(n)}
> ]
