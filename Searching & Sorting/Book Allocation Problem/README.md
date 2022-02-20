# Book Allocation Problem

---

### Problem Links
- **__GeeksForGeeks__** :point_right: https://practice.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1

### Solution
- **_solution.py_** :point_right: use binary search over range [1, sum(book_array)] and for each mid see if the given books array can be partitioned based on parts sum for given number of students **time-complexity O(Nlog(N))**, **space-complexity O(1)**.
