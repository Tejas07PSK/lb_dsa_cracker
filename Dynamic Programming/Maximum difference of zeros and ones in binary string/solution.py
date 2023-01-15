from math import inf
class Solution:
	def maxSubstring (self, s):
		trans_num = -1
		curr_max_sum = 0
		global_max_sum = -inf
		for ch in s:
		    trans_num = -1
		    if ch == '0': trans_num = 1
		    if ((curr_max_sum + trans_num) < trans_num): curr_max_sum = trans_num
		    else: curr_max_sum += trans_num
		    global_max_sum = max(global_max_sum, curr_max_sum)
		return global_max_sum
