from math import inf
class Solution:
    def heapify (self, arr, n, i):
        curr_ele, curr_idx = arr[i], i
        left_idx, right_idx = 2 * curr_idx + 1, 2 * curr_idx + 2
        left_ele = arr[left_idx] if (left_idx < n) else -inf
        right_ele = arr[right_idx] if (right_idx < n) else -inf
        while (not ((curr_ele >= left_ele) and (curr_ele >= right_ele))):
            if (right_ele > left_ele):
                arr[curr_idx], arr[right_idx] = right_ele, curr_ele
                curr_idx = right_idx
            else:
                arr[curr_idx], arr[left_idx] = left_ele, curr_ele
                curr_idx = left_idx
            curr_ele = arr[curr_idx]
            left_idx, right_idx = 2 * curr_idx + 1, 2 * curr_idx + 2
            left_ele = arr[left_idx] if (left_idx < n) else -inf
            right_ele = arr[right_idx] if (right_idx < n) else -inf

    def buildHeap (self, arr, n):
        for i in range((n - 1), -1, -1): self.heapify(arr, n, i)

    def HeapSort(self, arr, n):
        self.buildHeap(arr, n)
        while (n > 0):
            arr[0], arr[n - 1] = arr[n - 1], arr[0]
            self.heapify(arr, (n - 1), 0)
            n -= 1
