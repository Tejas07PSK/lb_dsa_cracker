class Solution:
    def findRotationPoint (self, nums, n):
        left, right = 0, n - 1
        while (left <= right):
            mid = left + ((right - left) // 2)
            if (nums[mid] <= nums[right]):
                if (nums[mid] < nums[mid - 1]):
                    right, left = mid - 1, mid
                    break
                right = mid - 1
            else:
                if (nums[mid] > nums[mid + 1]):
                    right, left = mid, mid + 1
                    break
                left = mid + 1
        return left, right
    
    def bin_search (self, nums, left, right, key):
        while (left <= right):
            mid = left + ((right - left) // 2)
            if (nums[mid] == key):
                return mid
            elif (key < nums[mid]):
                right = mid - 1
            else:
                left = mid + 1
        return -1

    def search (self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = self.findRotationPoint(nums, n)
        if ((right >= 0) and (target >= nums[0] and target <= nums[right])):
            return self.bin_search(nums, 0, right, target)
        else:
            return self.bin_search(nums, left, (n - 1), target)
