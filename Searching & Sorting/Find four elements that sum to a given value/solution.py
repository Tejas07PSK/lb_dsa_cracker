class Solution:
    def fourSum (self, arr, k):
        n = len(arr)
        arr.sort()
        result_set = set()
        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                low, high = j + 1, n - 1
                while (low < high):
                    target = arr[i] + arr[j] + arr[low] + arr[high]
                    if (target < k):
                        low += 1
                    elif (target > k):
                        high -= 1
                    else:
                        result_set.add((arr[i], arr[j], arr[low], arr[high]))
                        low += 1
                        high -= 1
        return sorted(result_set)
