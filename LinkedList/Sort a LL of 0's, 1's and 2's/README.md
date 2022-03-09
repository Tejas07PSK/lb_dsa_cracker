# Sort a LL of 0's, 1's and 2's

---

### Problem Links
- **__GeeksForGeeks__** :point_right: https://practice.geeksforgeeks.org/problems/given-a-linked-list-of-0s-1s-and-2s-sort-it/1

### Solution
- **_solution.py_** :point_right: traverse the original list and segregate it into seperate lists of 0s, 1s and 2s keep track of the heads and tails of these lists, in the end just merge them together (be careful with some corner cases here) and return the head to the modified list  **time-complexity O(N)**, **space-complexity O(1)**.
