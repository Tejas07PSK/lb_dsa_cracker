# Find four elements that sum to a given value

---

### Problem Links
- **__GeeksForGeeks__** :point_right: https://practice.geeksforgeeks.org/problems/find-all-four-sum-numbers1732/1

### Solution
- **_solution.py_** :point_right: first sort the array, then use 2 nested loops to fix first 2 points, then for 3rd and 4th points use 2 pointer technique inside the second loop, use a set to store the results to avoid duplicates, at last sort the result set **time-complexity O(N^3)**, **space-complexity O(N^2)**.
