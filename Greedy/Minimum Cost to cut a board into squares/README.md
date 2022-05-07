# Minimum Cost to cut a board into squares

---

### Problem Links
- **__GeeksForGeeks__** :point_right: https://practice.geeksforgeeks.org/problems/minimum-cost-to-cut-a-board-into-squares/1

### Solution
- **_solution.py_** :point_right: first sort the given sheet cutting prices arrays for column and row in descending order, then use simple 2 pointer technique (very similar to the one used in merging 2 sorted arrays), if selected element is from column array then multiply it's value with the number of row values iterated so far plus 1, do the exact opposite if the selected element is from row array **time-complexity O(Mlog(M) + Nlog(N))**, **space-complexity O(1)**.
