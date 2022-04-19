# Replace every element with the least greater element on its right

---

### Problem Links
- **__CodeStudio__** :point_right: https://www.codingninjas.com/codestudio/problems/least-greater-element_1164266?leftPanelTab=0

### Solution
- **_solution.py_** :point_right: use an AVL tree and while inserting and balancing keep track of last the inserted node's in-order successor **time-complexity O(nlog(n))**, **space-complexity O(n)**.
