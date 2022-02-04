# Find a pair with a given difference

---

### Problem Links
- **__GeeksForGeeks__** :point_right: https://practice.geeksforgeeks.org/problems/find-pair-given-difference1559/1

### Solution
- **_solution.py_** :point_right: first sort the array, then use binary-search on the right of every element, with key being the current element + given difference **time-complexity O(Nlog(N))**, **space-complexity O(1)**.
