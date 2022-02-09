# Merge 2 sorted arrays no extra space

---

### Problem Links
- **__GeeksForGeeks__** :point_right: https://practice.geeksforgeeks.org/problems/merge-two-sorted-arrays5135/1

### Solution
- **_solution1.py_** :point_right: use 2 pointer technique to put first n smallest elements in array1 and the remaining m largest elements in array2, finally sort both these arrays **time-complexity O(N+M+Nlog(N)+Mlog(M))**, **space-complexity O(1)**.
- **_solution2.py_** :point_right: use shell sort gap technique **time-complexity O((N+M)log(N+M))**, **space-complexity O(1)**.
