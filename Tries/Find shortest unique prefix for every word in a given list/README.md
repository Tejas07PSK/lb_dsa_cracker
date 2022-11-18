# Find shortest unique prefix for every word in a given list

---

### Problem Links
- **__GeeksForGeeks__** :point_right: https://practice.geeksforgeeks.org/problems/shortest-unique-prefix-for-every-word/1

### Solution
- **_solution.py_** :point_right: use a char frequency trie, first all words into this trie, and then for each word traverse the trie till the char having frequency 1, the prefix string so far is your answer **time-complexity O(N * length of each word)**, **space-complexity O(N * length of each word)**
