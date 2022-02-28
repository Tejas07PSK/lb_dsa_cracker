# Add 1 to a number represented as a Linked List

---

### Problem Links
- **__GeeksForGeeks__** :point_right: https://practice.geeksforgeeks.org/problems/add-1-to-a-number-represented-as-linked-list/1

### Solution
- **_solution.py_** :point_right: first reverse the given linked list, then set initial carry as 1, then keep adding the carry value to the node data while new carry is not zero and the end of the linked list has not been reached, finally reverse the linked list again and return the head **time-complexity O(N)**, **space-complexity O(1)**.
