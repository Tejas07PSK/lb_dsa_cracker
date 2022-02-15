# Aggressive cows

---

### Problem Links
- **__SPOJ__** :point_right: https://www.spoj.com/problems/AGGRCOW/

### Solution
- **_solution.py_** :point_right: first use binary search over range [1, maxElement(position_array)], consider each mid as minimum distance to seperate the cows, then start a linear search from index 1 in position array such that the total number of positions having value >= position_array[i] + mid is equal to total cows, if this count is not equal to total cows go towards left in range else go towards right **time-complexity O(Nlog(maxIn(position_array)))**, **space-complexity O(1)**.
