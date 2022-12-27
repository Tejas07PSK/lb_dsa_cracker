from bisect import bisect_left
class Solution:
    def longestSubsequence (self, arr, n):
        seq = [arr[0]]
        for i in range(1, len(arr)):
            if (arr[i] > seq[-1]): seq.append(arr[i])
            else: seq[bisect_left(seq, arr[i])] = arr[i]
        return len(seq)
