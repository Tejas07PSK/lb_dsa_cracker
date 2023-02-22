class Solution:
	def AllPossibleStrings (self, s):
		n = len(s)
		pwr_2_lim = 1
		res = []
		while (n > 0):
		    pwr_2_lim <<= 1
		    n -= 1
		pwr_2_lim = pwr_2_lim if (pwr_2_lim != 1) else (pwr_2_lim >> 1)
		for i in range(1, pwr_2_lim):
		    tmp_i, tmp_ch_arr, index = i, [], 0
		    while (tmp_i > 0):
		        if ((tmp_i & 1) == 1): tmp_ch_arr.append(s[index])
		        tmp_i >>= 1
		        index += 1
		    res.append("".join(tmp_ch_arr))
        res.sort()
		return res
