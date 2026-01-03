## How to traverse the tags, and nested children?

- recursive call. Search until the bottom of the nest.
- use stack to store the data. when we find the closing tag.

The stack of the recursive call depends on the nest depth of the html elements. For O(N). The number of the nodes. Also, the computing complexity is also O(N) because the recursive call is called every node.
