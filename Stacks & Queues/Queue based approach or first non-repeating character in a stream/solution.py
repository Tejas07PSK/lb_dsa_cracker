from collections import deque
class Solution:
	def FirstNonRepeating (self, A):
	    seen_already, q = {}, deque()
	    res = []
	    for ch in A:
	        q.append(ch)
	        if (ch not in seen_already): seen_already[ch] = 1
	        else: seen_already[ch] += 1
	        while ((q) and (seen_already[q[0]] > 1)): q.popleft()
	        if (not q): res.append('#')
	        else: res.append(q[0])
	    return "".join(res)
