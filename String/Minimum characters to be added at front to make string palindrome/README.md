# Minimum characters to be added at front to make string palindrome

---

### Problem Links
- **__GeeksForGeeks__** :point_right: https://www.geeksforgeeks.org/minimum-characters-added-front-make-string-palindrome/

### Solution
- **_solution.py_** :point_right: create a new string by adding a special character after original string and then adding the reverse of original string, next calculate the lps of this new string and get the value at last index, subtract this from the length of original string **time-complexity O(N)**, **space-complexity O(N)**.
