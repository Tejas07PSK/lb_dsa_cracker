# Find the inversion count

---

### Problem Links
- **__GeeksForGeeks__** :point_right: https://practice.geeksforgeeks.org/problems/inversion-of-array-1587115620/1

### Solution
- **_solution.py_** :point_right: use merge-sort technique, remember inversion-count of any element in an array is the number of elements smaller than it that have appeared after it in the original array, the sum of inversion counts of the individual elements of the array will be the inversion count of the entire array itself **time-complexity O(Nlog(N))**, **space-complexity O(N)**.
