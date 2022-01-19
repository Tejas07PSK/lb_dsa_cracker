# Given a sequence of words, print all anagrams together

---

### Problem Links
- **__GeeksForGeeks__** :point_right: https://practice.geeksforgeeks.org/problems/print-anagrams-together/1

### Solution
- **_solution.py_** :point_right: sort each word from the list and store it in a trie, whenever a word-end node is reached store the index of the original word from the original list, as part of a index-list parameter of the trie node **time-complexity O(NMlog(M))**, **space-complexity O(NM)**.
