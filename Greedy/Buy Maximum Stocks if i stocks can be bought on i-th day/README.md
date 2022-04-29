# Buy Maximum Stocks if i stocks can be bought on i-th day

---

### Problem Links
- **__CodeStudio__** :point_right: https://www.codingninjas.com/codestudio/problems/buy-maximum-stocks-if-i-stocks-can-be-bought-on-i-th-day_1169470?leftPanelTab=0

### Solution
- **_solution.py_** :point_right: create a temp array with tuples of stock values on ith days along with the index (i + 1) as the day limit, then sort this array based on the daily stock values, finaly use simple greedy logic **time-complexity O(Nlog(N))**, **space-complexity O(N)**.
