# Palindrome Partitioning Problem

---

### Problem Links
- **__GeeksForGeeks__** :point_right: https://practice.geeksforgeeks.org/problems/palindromic-patitioning4845/1
- **__LeetCode__** :point_right: https://leetcode.com/problems/palindrome-partitioning-ii/

### Solution
- **_solution1.py_** :point_right: use top-down dp with memoization **time-complexity O(N^3)**, **space-complexity O(N^2)**
- **_solution2.py_** :point_right: use top-down dp with memoization more optimized, first construct isPalindrome matrix for all substrings, then use word-break technique **time-complexity O(N^2)**, **space-complexity O(N^2 + N)**
- **_solution3.py_** :point_right: use bottom-up dp with tabulation, use same concept from previous solution **time-complexity O(N^2)**, **space-complexity O(N^2 + N)**
