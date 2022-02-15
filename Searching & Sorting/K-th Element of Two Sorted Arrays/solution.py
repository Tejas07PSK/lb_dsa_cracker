import math

class Solution:
    def kthElement (self, arr1, arr2, N, M, K):
        if (len(arr2) < len(arr1)):
            arr1, arr2, N, M = arr2, arr1, M, N
        low, high = 0, N - 1 ; ans = None
        while True:
            left_idx_arr1 = high + ((low - high) // 2) if (high < low) else low + ((high - low) // 2)
            if (left_idx_arr1 >= K):
                high = left_idx_arr1 - 1 ; continue
            right_idx_arr1 = left_idx_arr1 + 1 ; left_idx_arr2 = K - left_idx_arr1 - 2 ; right_idx_arr2 = left_idx_arr2 + 1
            left_ele_arr1 = -math.inf if left_idx_arr1 < 0 else math.inf if left_idx_arr1 >= N else arr1[left_idx_arr1]
            right_ele_arr1 = -math.inf if right_idx_arr1 < 0 else math.inf if right_idx_arr1 >= N else arr1[right_idx_arr1]
            left_ele_arr2 = -math.inf if left_idx_arr2 < 0 else math.inf if left_idx_arr2 >= M else arr2[left_idx_arr2]
            right_ele_arr2 = -math.inf if right_idx_arr2 < 0 else math.inf if right_idx_arr2 >= M else arr2[right_idx_arr2]
            if (left_ele_arr1 <= right_ele_arr2):
                if (left_ele_arr2 <= right_ele_arr1):
                    ans = max(left_ele_arr1, left_ele_arr2) ; break
                else:
                    low = right_idx_arr1
            else:
                high = left_idx_arr1 - 1
        return ans
