# Searching in an array where adjacent differ by at most k

---

### Problem Links
- **__GeeksForGeeks__** :point_right: https://www.geeksforgeeks.org/searching-array-adjacent-differ-k/

### Solution
- **_solution1.py_** :point_right: use simple linear search, but iteration amount should be i += max(1, (abs(key - arr[i]) // k)) **time-complexity O(N)**, **space-complexity O(1)**.
