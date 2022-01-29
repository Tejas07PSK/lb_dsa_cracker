# Search in a rotated sorted array

---

### Problem Links
- **__LeetCode__** :point_right: https://leetcode.com/problems/search-in-rotated-sorted-array/

### Solution
- **_solution1.py_** :point_right: first use binary search to find rotation points, then search on either half based on target value **time-complexity O(log(N))**, **space-complexity O(1)**.
- **_solution2.py_** :point_right: use binary search only once with custom conditions **time-complexity O(log(N))**, **space-complexity O(1)**.
