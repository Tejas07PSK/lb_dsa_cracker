# Smallest number with atleast n trailing zeroes infactorial

---

### Problem Links
- **__GeeksForGeeks__** :point_right: https://practice.geeksforgeeks.org/problems/smallest-factorial-number5929/1

### Solution
- **_solution.py_** :point_right: use binary search in range [1, 5*N], for each mid count the number of zeroes in it's factorial by counting the number of prime factors as 5 in it, now check if it is greater than or less than N and reduce the search space accordingly **time-complexity O(log2(N)log5(N))**, **space-complexity O(1)**.
