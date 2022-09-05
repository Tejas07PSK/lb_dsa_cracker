# Convert BST to Min Heap

---

### Problem Links
- **__CodeStudio__** :point_right: https://www.codingninjas.com/codestudio/problems/convert-bst-to-min-heap_920498

### Solution
- **_solution.py_** :point_right: first perform in-order traversal of the tree and store the result in a list, then perform pre-order traversal over the same tree while filling items from the previously created list **time-complexity O(N)**, **space-complexity O(N)**.
