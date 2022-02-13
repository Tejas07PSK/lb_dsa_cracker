# Kth smallest number again

---

### Problem Links
- **__HackerEarth__** :point_right: https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/kth-smallest-number-again-2/

### Solution
- **_solution.py_** :point_right: first sort the intervals array based on the start values, then merge the overlapping intervals using a stack, finally use linear search over the merged intervals array, to find the kth smallest number **time-complexity O(Nlog(N))**, **space-complexity O(N)**.
