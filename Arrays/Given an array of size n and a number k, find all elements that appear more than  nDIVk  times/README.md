# Given an array of size n and a number k, find all elements that appear more than  nDIVk  times

---

### Problem Links
- **_LeetCode_** :point_right: https://leetcode.com/problems/majority-element-ii/

### Solution
- **_solution.py_** :point_right: uses a modified variation of boyer-moore voting algorithm (used in tetris game also) search the internet for more details, used hashmap/dict as intermediate bucket instead of array to improve performance, size of the map will never exceed (K - 1) **time-complexity O(NK)**, **space-complexity O(K)** since K < N space used is approximately constant O(1).
