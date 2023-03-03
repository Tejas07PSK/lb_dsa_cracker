class Solution:
	def minJumps (self, arr, n):
	    i, jumps = 0, 0
	    while (i < (len(arr) - 1)):
	        if (arr[i] == 0): return -1
	        if ((i + arr[i]) >= (len(arr) - 1)): return (jumps + 1)
	        i = i + 1
	        for next_idx in range(i + 1, (i + arr[i - 1])):
	            if ((len(arr) - 1 - next_idx - arr[next_idx]) < (len(arr) - 1 - i - arr[i])):
	                i = next_idx
	        jumps += 1
	    return jumps
