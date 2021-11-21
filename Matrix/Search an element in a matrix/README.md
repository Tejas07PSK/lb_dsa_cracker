# Search an element in a matrix

---

### Problem Links
- **__LeetCode__** :point_right: https://leetcode.com/problems/search-a-2d-matrix/

### Solution
- **_solution.py_** :point_right: use binary-search over rows to find a potential row and then apply binary-search over columns, on that row to find the target **time-complexity O(log(R)log(C))**, **space-complexity O(1)**.
