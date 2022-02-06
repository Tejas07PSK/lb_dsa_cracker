class Solution:
    def countTriplets (self, arr, n, sum):
        arr.sort()
        count = 0
        for i in range(n - 2):
            low, high = i + 1, n - 1
            while (low < high):
                target = arr[i] + arr[low] + arr[high]
                if (target < sum):
                    count += (high - low)
                    low += 1
                else:
                    high -= 1
        return count
