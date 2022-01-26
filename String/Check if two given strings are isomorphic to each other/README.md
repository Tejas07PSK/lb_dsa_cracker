# Check if two given strings are isomorphic to each other

---

### Problem Links
- **__GeeksForGeeks__** :point_right: https://practice.geeksforgeeks.org/problems/isomorphic-strings-1587115620/1
- **__LeetCode__** :point_right: https://leetcode.com/problems/isomorphic-strings/

### Solution
- **_solution.py_** :point_right: use a hash-map to store character mapping from string A to B, also use a set to check which all characters from B have already been mapped, remaining logic is pretty straight forward **time-complexity O(A+B)**, **space-complexity O(1)**.
