class Solution:
	def setBits (self, N):
	    count = 0
	    while (N > 0):
	        if ((1 & N) == 1): count += 1
	        N >>= 1
	    return count
