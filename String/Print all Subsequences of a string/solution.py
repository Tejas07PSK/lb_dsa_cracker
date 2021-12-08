class Solution:
    def subsets (self, nums: List[int]) -> List[List[int]]:
        n = len(nums) ; lim = 2 ** n
        i = 0 ; res = []
        while (i < lim):
            tmp_res = []
            mask, j = 1, 1
            while (j <= n):
                if ((i & mask) != 0):
                    tmp_res.append(nums[j - 1])
                mask <<= 1 ; j += 1
            res.append(tmp_res)
            i += 1
        return res
