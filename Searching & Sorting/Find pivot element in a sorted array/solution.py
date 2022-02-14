class Solution:
    def findMin (self, nums: List[int]) -> int:
        n = len(nums) ; low, high = 0, n - 1
        mid = None
        while (low < high):
            mid = low + ((high - low) // 2)
            if (nums[mid] <= nums[high]):
                high = mid
            else:
                low = mid + 1
        return nums[low]
