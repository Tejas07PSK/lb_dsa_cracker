# Find the triplet that sum to a given value

---

### Problem Links
- **_GeeksForGeeks_** :point_right: https://practice.geeksforgeeks.org/problems/triplet-sum-in-array-1587115621/1#

### Solution
- **_solution.py_** :point_right: sort the array, then run an outer loop till (N - 3) fixing one number at a time, use a nested inner loop with two pointers to find 2 possible numbers, if these numbers add up to expected sum then break the loops and return the answer, **time-complexity O(N^2)**, **space-complexity O(1)**.
