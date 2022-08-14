# LRU Cache Implementation

---

### Problem Links
- **__GeeksForGeeks__** :point_right: https://practice.geeksforgeeks.org/problems/lru-cache/1

### Solution
- **_solution.py_** :point_right: use a hash-map to fetch cache entries fast, by mapping the key entires with it's corresponding nodes in DLL, use a DLL queue to maintian the order of node accesses and deletions, last accessed node is always moved to the end of DLL and when capacity of cache is full, the first node in the DLL is removed (as this is the least used) and the new node is entered at the end, kind of like a queue **time-complexity O(1) for set and get**, **space-complexity O(N) for the underlying hash-map and DLL, O(1) for set and get**.
