# Median in a stream of Integers

---

### Problem Links
- **__GeeksForGeeks__** :point_right: https://practice.geeksforgeeks.org/problems/find-median-in-a-stream-1587115620/1

### Solution
- **_solution.py_** :point_right: use a max-heap to store the left most elements and a min-heap to store the right most elements, as they would appear if the stream was sorted, then use some ad-hoc balancing logic, look at code **time-complexity O(NlogN)**, **space-complexity O(N)**.
