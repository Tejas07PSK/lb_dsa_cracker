# Count of number of given string in 2D character array

---

### Problem Links
- **__GeeksForGeeks__** :point_right: https://www.geeksforgeeks.org/find-count-number-given-string-present-2d-character-array/

### Solution
- **_solution.py_** :point_right: traverse through the character matrix, whenever the start character of the given string is encountered, apply recursive dfs in 4 adjacent directions (up, down, left right) **time-complexity O(RC4^S)**, **space-complexity O(1)**.
