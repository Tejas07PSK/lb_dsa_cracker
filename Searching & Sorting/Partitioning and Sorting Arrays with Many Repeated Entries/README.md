# Partitioning and Sorting Arrays with Many Repeated Entries

---

### Problem Links
- **__Baeldung__** :point_right: https://www.baeldung.com/java-sorting-arrays-with-repeated-entries

### Solution
- **_solution1.py_** :point_right: use standard 2-way quick-sort with random pivot selection, this technique will work best when we don't have too many duplicates in the given array or if most/all elements in the array are unique **time-complexity O(Nlog(N))**, **space-complexity O(1)**.
- **_solution2.py_** :point_right: use standard 3-way quick-sort with random pivot selection, this technique will work best when we have too many duplicates in the given array or if most/all elements in the array are not unique **time-complexity O(Nlog(N))**, **space-complexity O(1)**.
