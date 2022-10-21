# Minimum time taken by each job to be completed given by a Directed Acyclic Graph

---

### Problem Links
- **__GeeksForGeeks__** :point_right: https://practice.geeksforgeeks.org/problems/minimum-time-taken-by-each-job-to-be-completed-given-by-a-directed-acyclic-graph/1

### Solution
- **_solution.py_** :point_right: use kahn's bfs topological sort algo, but traverse level by level while inside queue loop, each level will correspond to the current time **time-complexity O(V+E)**, **space-complexity O(V)**.
