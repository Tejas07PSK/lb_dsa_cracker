# Check if 2 trees are mirror or not

---

### Problem Links
- **__GeeksForGeeks__** :point_right: https://practice.geeksforgeeks.org/problems/check-mirror-in-n-ary-tree1528/1

### Solution
- **_solution.py_** :point_right: use a hash-map to store a node and it's stack of children for the first tree, now for every node encountered in second tree, check if it exists in the hash-map, if it does check if the last element popped form the stack is equal to the child of the current second tree node, repeat until end of second tree is reached **time-complexity O(E)**, **space-complexity O(NE)**.
