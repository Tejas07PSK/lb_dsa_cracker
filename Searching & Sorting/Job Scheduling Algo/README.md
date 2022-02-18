# Job Scheduling Algo

---

### Problem Links
- **__GeeksForGeeks__** :point_right: https://www.geeksforgeeks.org/weighted-job-scheduling-log-n-time/
- **__LeetCode__** :point_right: https://leetcode.com/problems/maximum-profit-in-job-scheduling/

### Solution
- **_solution1.py_** :point_right: use standard bottom-up dynamic-programming **time-complexity O(N^2)**, **space-complexity O(N)**.
- **_solution2.py_** :point_right: optimize above approach with binary search, in which we search for the last non-overlapping job from the left, within outer-loop of jobs array starting from index 1 **time-complexity O(Nlog(N))**, **space-complexity O(N)**.
