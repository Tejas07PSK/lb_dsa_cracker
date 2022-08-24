# Minimum sum of squares of character counts in a given string after removing “k” characters

---

### Problem Links
- **__GeeksForGeeks__** :point_right: https://practice.geeksforgeeks.org/problems/game-with-string4100/1

### Solution
- **_solution.py_** :point_right: first store the character counts in a hashmap, then heapify the count values into a max heap, then start popping from the max heap, decrease the current count and repush it into the max heap, until the character deletion limit is zero, finally loop through the remaining values in the heap, squaring and adding them to the answer  **time-complexity O(Nlog(N))**, **space-complexity O(N)**.
