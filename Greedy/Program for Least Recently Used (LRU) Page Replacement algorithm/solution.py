from collections import deque
class Solution:
    def pageFaults (N, C, pages):
        indexes_vals, page_set, page_faults, ini_cap = deque(), set(), 0, 0
        for i in range(N):
            if (pages[i] not in page_set):
                page_faults += 1
                if (ini_cap < C):
                    page_set.add(pages[i]) ; indexes_vals.append((i, pages[i])) ; ini_cap += 1
                else:
                    while (indexes_vals[0][1] not in page_set): indexes_vals.popleft()
                    page_set.remove(indexes_vals.popleft()[1]) ; page_set.add(pages[i]) ; indexes_vals.append((i, pages[i]))
            else:
                indexes_vals.append((i, pages[i]))
            if (ini_cap < C):
                ini_cap += 1
            if (pages[i] not in page_set):
                page_faluts += 1
                if ()
                
