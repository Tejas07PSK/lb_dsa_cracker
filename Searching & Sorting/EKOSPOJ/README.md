# EKOSPOJ

---

### Problem Links
- **__SPOJ__** :point_right: https://www.spoj.com/problems/EKO/

### Solution
- **_solution.py_** :point_right: use binary-search over range [0, max(tree_height_array)], take each mid as height of saw-blade and see if you cut the trees in a way such that total wood gained by cutting, is at-least equal to the given target quantity **time-complexity O(Nlog(max(tree_height_array)))**, **space-complexity O(1)**.
