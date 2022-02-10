# Bishu and Soldiers

---

### Problem Links
- **__HackerEarth__** :point_right: https://www.hackerearth.com/problem/algorithm/bishu-and-soldiers-227/

### Solution
- **_solution.py_** :point_right: first sort the power array of soldiers, then use binary search to find the rightmost entry point of bishu's power in the soldiers power array for each round, also pre-calculate the prefix sum of the power array of soldiers **time-complexity O((Q + N)log(N))**, **space-complexity O(N)**.
