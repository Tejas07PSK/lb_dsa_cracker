# Find if there is a path of more than k length from a source

---

### Problem Links
- **__GeeksForGeeks__** :point_right: https://practice.geeksforgeeks.org/problems/path-of-greater-than-equal-to-k-length1034/1

### Solution
- **_solution.py_** :point_right: use dfs with backtracking, be careful about multiple edges between same two nodes, in this case always take the edge with the max weight, because in the constraints we are told edge weight can never be negative and we will be adding such paths eventually, to get total traversed length at least >= k **time-complexity O(V!)**, **space-complexity O(V^2)**.
