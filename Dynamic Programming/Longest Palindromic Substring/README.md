# Longest Palindromic Substring

---

### Problem Links
- **__GeeksForGeeks__** :point_right: https://practice.geeksforgeeks.org/problems/longest-palindrome-in-a-string1956/1

### Solution
- **_solution1.py_** :point_right: use top-down dp with memoization **time-complexity O(S^2)**, **space-complexity O(S^2)**
- **_solution2.py_** :point_right: use bottom-up dp with tabulation **time-complexity O(S^2)**, **space-complexity O(S^2)**
- **_solution3.py_** :point_right: use bottom-up dp with tabulation, space-optimized **time-complexity O(S^2)**, **space-complexity O(S)**
- **_solution4.py_** :point_right: use expand around centres approach, treat each char plus gap after it as centres for palindrome string **time-complexity O(S^2)**, **space-complexity O(1)**
- **_solution5.py_** :point_right: use Manacher's Algorithm **time-complexity O(S)**, **space-complexity O(S)**
