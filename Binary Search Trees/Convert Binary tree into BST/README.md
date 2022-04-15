# Convert Binary tree into BST

---

### Problem Links
- **__GeeksForGeeks__** :point_right: https://practice.geeksforgeeks.org/problems/binary-tree-to-bst/1

### Solution
- **_solution.py_** :point_right: use in-order traversal over given binary tree, store the result in an array, then sort that array and re-traverse the binary tree using in-order traversal, only this time overwrite the node values with values from the sorted array **time-complexity O(N)**, **space-complexity O(N)**.
