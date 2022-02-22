# Subset Sums

---

### Problem Links
- **__SPOJ__** :point_right: https://www.spoj.com/problems/SUBSUMS/

### Solution
- **_solution.py_** :point_right: first divide the given array into 2 parts and generate the subset sum array for each of them, now sort the second subset sum array and for each element in the first subset sum array check if the following range [A - ssa1[i], B - ssa1[i]] exists in the second one, if it does count the difference between the start and end position **time-complexity O((N/2)2^(N/2))**, **space-complexity O(2^(N/2))**.
