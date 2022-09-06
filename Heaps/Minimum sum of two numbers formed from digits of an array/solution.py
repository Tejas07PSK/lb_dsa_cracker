from heapq import heapify, heappop
class Solution:
    def solve (self, arr, n):
        num1, num2 = 0, 0
        heapify(arr)
        while (len(arr) >= 2):
            num1 = num1 * 10 + heappop(arr)
            num2 = num2 * 10 + heappop(arr)
        if (len(arr) == 1): num1 = num1 * 10 + heappop(arr)
        return (num1 + num2)
