# Maximum size rectangle

---

### Problem Links
- **_GeeksForGeeks_** :point_right: https://practice.geeksforgeeks.org/problems/max-rectangle/1
- **_LeetCode_** :point_right: https://leetcode.com/problems/maximal-rectangle/

### Solution
- **_solution.py_** :point_right: uses max size rectangle in histogram technique, before proceeding pre-process the given matrix, such that any index in a row (apart from row 1) contains the sum of value at this index and value at this index in previous row, provided current value is not zero **time-complexity O(RC)**, **space-complexity O(C)**.
