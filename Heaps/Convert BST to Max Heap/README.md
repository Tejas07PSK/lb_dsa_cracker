# Convert BST to Max Heap

---

### Problem Links
- **__GeeksForGeeks__** :point_right: https://practice.geeksforgeeks.org/problems/bst-to-max-heap/1

### Solution
- **_solution.py_** :point_right: first perform in-order traversal of the tree and store the result in a list, then perform post-order traversal over the same tree while filling items from the previously created list in reverse **time-complexity O(N)**, **space-complexity O(N)**.
