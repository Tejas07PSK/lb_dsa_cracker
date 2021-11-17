import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        if ((n1 == 0) and (n2 == 0)):
            return 0
        if (n1 > n2):
            nums1, nums2 = nums2, nums1
            n1, n2 = n2, n1
        if (n2 == 0):
            return ((nums1[(n1 - 1) // 2] + nums1[(n1 + 1) // 2]) / 2) if ((n1 % 2) == 0) else nums1[(n1 - 1) // 2]
        left, right = 0, (n1 - 1)
        half_size = ((n1 + n2 + 1) // 2)
        while True:
            mid = (right + ((left - right) // 2)) if (right < left) else (left + ((right - left) // 2))
            left_element_1_from_nums1 = -math.inf if (mid < 0) else  nums1[mid]
            right_element_1_from_nums1 = math.inf if ((mid + 1) >= n1) else nums1[mid + 1]
            left_element_2_from_nums2 = -math.inf if ((half_size - mid - 2) < 0) else nums2[half_size - mid - 2]
            right_element_2_from_nums2 = math.inf if ((half_size - mid - 1) >= n2) else  nums2[half_size - mid - 1]
            if ((left_element_1_from_nums1 <= right_element_2_from_nums2) and (left_element_2_from_nums2 <= right_element_1_from_nums1)):
                return ((max(left_element_1_from_nums1, left_element_2_from_nums2) + min(right_element_1_from_nums1, right_element_2_from_nums2)) / 2) if (((n1 + n2) % 2) == 0) else max(left_element_1_from_nums1, left_element_2_from_nums2)
            elif (left_element_1_from_nums1 > right_element_2_from_nums2):
                right = (mid - 1)
            else:
                left = (mid + 1)
        return (0)
