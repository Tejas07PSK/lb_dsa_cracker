# Write a program to find the longest Palindrome in a string.[ Longest palindromic Substring]

---

### Problem Links
- **__LeetCode__** :point_right: https://leetcode.com/problems/longest-palindromic-substring/
- **__GeeksForGeeks__** :point_right: https://practice.geeksforgeeks.org/problems/longest-palindrome-in-a-string3411/1

### Solution
- **_solution1.py_** :point_right: use bottom up dp, with diagonal pre-processing **time-complexity O(N^2)**, **space-complexity O(N^2)**.
- **_solution2.py_** :point_right: consider each point and gap between points as centers, then try to find the max size palindrome around those **time-complexity O(N^2)**, **space-complexity O(1)**. 
- **_solution3.py_** :point_right: use Manacher's algorithm **time-complexity O(N)**, **space-complexity O(N)**
