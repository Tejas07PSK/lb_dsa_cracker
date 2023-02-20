class Solution:
	def singleNumber (self, nums):
	    xor_chain = 0
	    for num in nums: xor_chain ^= num
	    xor_chain &= -xor_chain
	    nr_nums = [0, 0]
	    for num in nums:
	        if ((xor_chain & num) == 0): nr_nums[0] ^= num
	        else: nr_nums[1] ^= num
	    nr_nums.sort()
	    return nr_nums
