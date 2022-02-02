# Find the repeating and the missing

---

### Problem Links
- **__GeeksForGeeks__** :point_right: https://practice.geeksforgeeks.org/problems/find-missing-and-repeating2512/1

### Solution
- **_solution.py_** :point_right: idea is to use individual values as index, the one with repetition will try to access same index twice and will get caught. The catch is that there will be one unaccessed element in the array and bingo this is the one who's corresponding value is missing in the array **time-complexity O(N)**, **space-complexity O(1)**.
