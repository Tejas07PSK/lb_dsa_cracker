# Optimum location of point to minimize total distance

---

### Problem Links
- **__GeeksForGeeks__** :point_right: https://www.geeksforgeeks.org/optimum-location-point-minimize-total-distance/

### Solution
- **_solution.py_** :point_right: use ternary search over a big range of x-axis from -ve to +ve end, such that those points along their corresponding y-axis points satisfy the given line equation and are minimally distant from the given set of points **time-complexity O(CP)**, **space-complexity O(P)**, where C is a constant and is equal to log3(large_finite_search_space).
