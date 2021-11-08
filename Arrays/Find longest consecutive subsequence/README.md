# Find longest consecutive subsequence

---

### Problem Links
- **_GeeksForGeeks_** :point_right: https://practice.geeksforgeeks.org/problems/longest-consecutive-subsequence2449/1
- **_LeetCode_** :point_right: https://leetcode.com/problems/longest-consecutive-sequence/

### Solution
- **_solution1.py_** :point_right: sort list and then find consecuitve subsequence with max length, **time-complexity O(NlogN)**, **space-complexity O(1)**.
- **_solution2.py_** :point_right: convert list to hash-set, then find the start of a consecuitve subsequence, count till you find the last element in the sequence, repeat to find other sequences and overall max length, **time-complexity O(N)**, **space-complexity O(N)**.
