# Huffman Coding

---

### Problem Links
- **__GeeksForGeeks__** :point_right: https://practice.geeksforgeeks.org/problems/huffman-encoding3345/1

### Solution
- **_solution.py_** :point_right: create custom tree-nodes for all the given characters, which would store the character itself and it's corresponding frequencies, now push these nodes into a min-heap, once done keep poping 2 nodes at a time from the heap and merge their frequencies into a parent node with the current nodes being it's left and right child respectively, now push this parent node back into the min-heap, keep repeating until the heap contains only one node, pop this node as this will be the root of the huffman tree, now do a simple pre-order traversal of this tree, with some ad-hoc logic to get the character codes **time-complexity O(Nlog(N))**, **space-complexity O(N)**.
