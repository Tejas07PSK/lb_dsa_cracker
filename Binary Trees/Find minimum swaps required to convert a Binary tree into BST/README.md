# Find minimum swaps required to convert a Binary tree into BST

---

### Problem Links
- **__GeeksForGeeks__** :point_right: https://www.geeksforgeeks.org/minimum-swap-required-convert-binary-tree-binary-search-tree/

### Solution
- **_solution.py_** :point_right: first generate in-order traversal array of the given partial BST, then use the graph-loop detection technique, like the one used in finding the minimum number of swaps to make array sorted, finally print the swap count **time-complexity O(Nlog(N))**, **space-complexity O(N)**.
