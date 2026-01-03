## Why bidirectional BFS must expand level by level

In Breadth-First Search (BFS), nodes are explored in increasing order of distance from the start node.
This means that all nodes at distance *d* are processed before any node at distance *d + 1*.

In a **single-source BFS**, this property automatically guarantees that the first time we reach the goal,
we have found the shortest path.

However, in **bidirectional BFS**, we run two BFS processes at the same time:

* one forward from the start node
* one backward from the goal node

If we expand nodes **one by one** from each side, the two searches may progress to **different depths**.
For example, one side might already be exploring nodes at distance 3, while the other side is still at distance 1.

If the searches meet in this situation,
the meeting point does **not necessarily correspond to the shortest path**.
A deeper meeting can be found earlier simply because one side expanded faster,
not because the path is shorter.

To avoid this problem, bidirectional BFS must expand **one full level at a time** on each side.

Expanding *one level* means:

* processing all nodes at the current distance
* and only then moving on to nodes at the next distance

By doing this, both searches advance in a synchronized way, and the first intersection guarantees that
the sum of distances from the start and the goal is minimal.

In short:

> **Bidirectional BFS must expand level by level to preserve the shortest-path guarantee.**

### Short version (for comments / interviews)

> In bidirectional BFS, expanding one node at a time can cause the two searches to reach different depths.
> This may lead to finding a meeting point that is not on the shortest path.
> Expanding one full level at a time keeps both searches synchronized and guarantees that the first meeting point corresponds to the shortest path.


## Why expanding the smaller frontier first makes sense

Yes — the idea really *is* that simple.

In bidirectional BFS, we already guarantee correctness by expanding the search **level by level** on both sides.
That level synchronization is what ensures we find a shortest path.

Once that guarantee is in place, the remaining question is purely about **cost**.

At each step, we can choose to expand either:

* the frontier from the start side, or
* the frontier from the goal side.

Expanding a frontier costs roughly proportional to its size.
So if one frontier is much smaller than the other, expanding the smaller one is simply cheaper.

If the searches happen to meet while expanding the smaller frontier, that’s essentially a bonus:
we find the shortest path earlier *and* we paid less work to get there.

If they don’t meet yet, nothing is lost — the other frontier will be expanded later at the same depth, and the shortest-path guarantee is still preserved.

In other words:

> **Correctness comes from level-by-level expansion.
> Efficiency comes from expanding the smaller frontier first.**

This optimization does not change the algorithm’s behavior or guarantees.
It only reduces the amount of work done in practice.

---

### One-sentence summary

> In bidirectional BFS, expanding the smaller frontier first minimizes work without affecting correctness, because shortest-path guarantees are already enforced by level-synchronized expansion.

---

If you want, I can also rewrite this in a **more formal academic style** or a **casual README-style explanation**.
