# Cheapest Flights Within K Stops

---

### Problem Links
- **__LeetCode__** :point_right: https://leetcode.com/problems/cheapest-flights-within-k-stops/

### Solution
- **_solution1.py_** :point_right: use bfs with dijkstra's technique of maintaing a vertex array, in which we'll store the minimum total weight required to reach a vertex, look at code to understand better **time-complexity O(V+E)**, **space-complexity O(V+E)**.
- **_solution2.py_** :point_right: use straightforward bellman-ford algo k timees **time-complexity O(KE)**, **space-complexity O(V)**.
