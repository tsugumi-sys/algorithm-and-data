# Why `_heapify()` Runs in **O(n)**

*(GitHub-compatible, no LaTeX)*

This explanation uses one consistent definition of height so the math and the intuition align perfectly.

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

This definition matches the actual behavior of sift-down:

* Nodes at height 0 never move.
* A node at height `h` can move down at most `h` times.
* The root (height `H`) has the largest possible movement.

---

# 2. Number of Nodes at Height `h` (Why n / 2^(h+1)?)

A binary heap is a **complete binary tree**.

* The bottom level contains roughly `n/2` of all nodes.
* The next level contains about `n/4`.
* Then `n/8`, and so on.

So the number of nodes at height `h` (counted from the bottom) is approximately:

```
nodes(h) ≈ n / 2^(h+1)
```

Example:

```
h = 0  → about n/2 nodes
h = 1  → about n/4 nodes
h = 2  → about n/8 nodes
...
h = H  → 1 node (the root)
```

Reason this works:
Each higher level has half as many nodes as the level below it, and height `h` is simply “how many levels above the bottom” that node sits.

---

# 3. Cost per Node at Height `h`

A node at height `h` can sift down at most `h` levels.

Thus:

```
cost_per_node(h) = h
```

Examples:

* Leaves (h = 0) → cost 0
* Nodes one level above leaves (h = 1) → cost 1
* Root (h = H) → cost H

This height definition perfectly matches sift-down behavior.

---

# 4. Total Cost of `_heapify()`

Total work = sum of (number of nodes at height `h`) × (cost per node):

```
T(n) ≈ sum over h=0..H of  (n / 2^(h+1)) * h
```

Factor out `n`:

```
T(n) ≈ n * sum over h=0..∞ of  (h / 2^(h+1))
```

Now we evaluate the remaining infinite sum.

---

# 4.1 Proof of the Identity

`sum(h / 2^h) = 2`

Below are two proofs you asked to integrate, written in GitHub-friendly format.

---

## Proof 1: Using a Known Power Series Formula (公式から一発)

1. Start with the geometric series:

```
sum_{h=0..∞} x^h = 1 / (1 - x)    for |x| < 1
```

2. Differentiate both sides:

```
sum_{h=1..∞} h * x^(h-1) = 1 / (1 - x)^2
```

3. Multiply by `x`:

```
sum_{h=1..∞} h * x^h = x / (1 - x)^2
```

4. Substitute `x = 1/2`:

```
sum_{h=1..∞} (h / 2^h)
= (1/2) / (1/2)^2
= (1/2) / (1/4)
= 2
```

Done.

---

## Proof 2: Rearrangement Trick (並べ替えトリック)

Let:

```
S = sum_{h=1..∞} (h / 2^h)
  = 1/2 + 2/4 + 3/8 + 4/16 + ...
```

Compute S/2:

```
S/2 = 1/4 + 2/8 + 3/16 + 4/32 + ...
```

Now subtract term-wise:

```
S - S/2
= (1/2 - 0)
+ (2/4 - 1/4)
+ (3/8 - 2/8)
+ (4/16 - 3/16)
+ ...
```

This simplifies to:

```
S/2 = 1/2 + 1/4 + 1/8 + 1/16 + ...
```

The right-hand side is a geometric series with sum 1.
Therefore:

```
S/2 = 1  →  S = 2
```

---

# 4.2 Apply the Identity to Heapify

We had:

```
T(n) ≈ n * sum(h / 2^(h+1))
```

Noting:

```
sum(h / 2^(h+1)) = (1/2) * sum(h / 2^h) = (1/2) * 2 = 1
```

So:

```
T(n) ≈ n * 1 = n
```

Thus heapify runs in:

```
O(n)
```

---

# 5. Intuition (No Math Needed)

Think in terms of contribution from each height:

* About `n/2` nodes are leaves → cost 0
* About `n/4` nodes might move 1 level
* About `n/8` nodes might move 2 levels
* About `n/16` nodes might move 3 levels
* …

Cost goes up, but number of nodes goes down at the same rate.
These cancel out, producing total work proportional to `n`.

---

# 6. Final Summary

* Height `h` counts from the bottom (leaves = 0).
* Nodes at height `h` ≈ `n / 2^(h+1)`.
* Cost per node at height `h` = `h`.
* The key identity `sum(h / 2^h) = 2` yields linear total work.

```
Bottom-up heap construction runs in O(n) time.
```
