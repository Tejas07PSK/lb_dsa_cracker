# CHOCOLA – Chocolate

---

### Problem Links
- **__SPOJ__** :point_right: https://www.spoj.com/problems/CHOCOLA/

### Solution
- **_solution.py_** :point_right: first sort the given chocolate cutting prices arrays for column and row in descending order, then use simple 2 pointer technique (very similar to the one used in merging 2 sorted arrays), if selected element is from column array then multiply it's value with the number of row values iterated so far plus 1, do the exact opposite if the selected element is from row array **time-complexity O(Mlog(M) + Nlog(N))**, **space-complexity O(1)**.
