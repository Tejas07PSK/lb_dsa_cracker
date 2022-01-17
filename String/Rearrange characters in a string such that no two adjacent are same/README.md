# Rearrange characters in a string such that no two adjacent are same

---

### Problem Links
- **__GeeksForGeeks__** :point_right: https://practice.geeksforgeeks.org/problems/rearrange-characters4649/1/

### Solution
- **_solution1.py_** :point_right: use a max-heap to store string characters based on their frequency, then pop 2 nodes from the heap at a time and fill those characters one at a time in the result string, reduce their frequency and push them back to heap, repeat until length of the original string **time-complexity O(Nlog(N))**, **space-complexity O(N)**.
- **_solution2.py_** :point_right: use a hash-map/dict to store the frequency of the string characters, then fill max frequency character in even positions of the result string until it's frequency becomes zero, then fill the remaining characters first in the pending even positions and then in all the odd positions in the result string, until their frequencies become zero too **time-complexity O(N)**, **space-complexity O(N)**.
