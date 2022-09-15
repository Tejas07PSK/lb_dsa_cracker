# Making wired Connections

---

### Problem Links
- **__LeetCode__** :point_right: https://leetcode.com/problems/number-of-operations-to-make-network-connected/

### Solution
To minimally connect N nodes we need at least (N - 1) edges, also if a graph has k connected componenets, we need at least (k - 1) edges to join them together. Use this info to proceed with the below 2 solutions,
- **_solution1.py_** :point_right: use straightforward dfs **time-complexity O(V+E)**, **space-complexity O(V)**.
- **_solution2.py_** :point_right: use straightforward bfs **time-complexity O(V+E)**, **space-complexity O(V)**.
