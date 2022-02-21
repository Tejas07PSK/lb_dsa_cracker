# ROTI-Prata SPOJ

---

### Problem Links
- **__SPOJ__** :point_right: https://www.spoj.com/problems/PRATA/

### Solution
- **_solution.py_** :point_right: make observation over given constraints then take binary search range as [1, 1e7], take each mid as max allowed time-sum and calculate the number of parathas that can made using AP quadratic formula, based on this count accordingly traverse the left or right search space **time-complexity O(Llog(1e7))**, **space-complexity O(1)**.
