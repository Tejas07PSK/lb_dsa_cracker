class Solution:  
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        index_sum = [nums[0]]
        for i in range(1, n):
            index_sum.append(index_sum[i - 1] + nums[i])
        res = (n + 1)
        for i in range(n):
            left, right = i, (n - 1)
            while (left <= right):
                mid =  left + ((right - left) // 2)
                sum_upto_mid = (index_sum[mid] - index_sum[i] + nums[i])
                if (sum_upto_mid == target):
                    res = min(res, (mid - i + 1))
                    break
                elif (sum_upto_mid > target):
                    res = min(res, (mid - i + 1))
                    right = (mid - 1)
                else:
                    left = (mid + 1)
        return (0 if res == (n + 1) else res)
