# Longest Common Prefix

---

### Problem Links
- **__LeetCode__** :point_right: https://leetcode.com/problems/longest-common-prefix/

### Solution
- **_solution1.py_** :point_right: use standard brute-force, with vertical character scanning **time-complexity O(NM)**, **space-complexity O(1)**.
- **_solution2.py_** :point_right: reduce the number of comparisons, by applying binary-search over minimum length string, for each such prefix check if the other strings start with it **time-complexity O(NMlog(M))**, **space-complexity O(1)**.
- **_solution3.py_** :point_right: further reduce the number of comparisons, by using prefix-trie **time-complexity O(NM + M)**, **space-complexity O(NM)**.
