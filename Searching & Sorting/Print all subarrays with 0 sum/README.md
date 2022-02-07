# Print all subarrays with 0 sum

---

### Problem Links
- **__GeeksForGeeks__** :point_right: https://practice.geeksforgeeks.org/problems/zero-sum-subarrays1825/1

### Solution
- **_solution.py_** :point_right: keep calculating the prefix-sum till every index, if this value is zero increment counter by 1, if this sum was not seen before  then store this sum with frequency 1 in a hash-map else increment count by previous frequency of this sum in hash-map and increment the frequency of this sum by 1 in the hash-map **time-complexity O(N)**, **space-complexity O(N)**.
