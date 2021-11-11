class Solution:
    def trappingWater (self, arr, N):
        left, right, max_left, max_right = 0, (N - 1), 0, 0
        tot_water = 0
        while (left < right):
            if (arr[left] <= arr[right]):
                if (arr[left] >= max_left):
                    max_left = arr[left]
                else:
                    tot_water += (max_left - arr[left])
                left += 1
            else:
                if (arr[right] >= max_right):
                    max_right = arr[right]
                else:
                    tot_water += (max_right - arr[right])
                right -= 1
        return tot_water
