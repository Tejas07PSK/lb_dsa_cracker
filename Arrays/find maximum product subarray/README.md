# find maximum product subarray

---

### Problem Links
- **_GeeksForGeeks_** :point_right: https://practice.geeksforgeeks.org/problems/maximum-product-subarray3604/1
- **_LeetCode_** :point_right: https://leetcode.com/problems/maximum-product-subarray/

### Solution
- **_solution.py_** :point_right: almost similar to kadane's algo, but since 2 negative nums can yield a positive number when multiplied, we need to keep track of the subarray with the minimum sum so-far also, **time-complexity O(N)**, **space-complexity O(1)**.
