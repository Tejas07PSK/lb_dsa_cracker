# Count triplets in a sorted DLL whose sum is equal to given value “X”

---

### Problem Links
- **__GeeksForGeeks__** :point_right: https://www.geeksforgeeks.org/count-triplets-sorted-doubly-linked-list-whose-sum-equal-given-value-x/

### Solution
- **_solution.py_** :point_right: use outer loop to fix a node each time and then use 2 pointer technique on it's right side, to find two more points which can form a triplet having sum as X **time-complexity O(N^2)**, **space-complexity O(1)**.
