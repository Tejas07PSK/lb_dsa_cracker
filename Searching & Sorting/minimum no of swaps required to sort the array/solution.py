class Solution:
    def minSwaps(self, nums):
        n = len(nums)
        srt_arr_eiv = [[nums[i], i, False] for i in range(n)]
        srt_arr_eiv.sort(key=lambda x : x[0])
        swaps = 0
        for i in range(n):
            if (srt_arr_eiv[i][1] == i):
                srt_arr_eiv[i][2] = True
                continue
            if (srt_arr_eiv[i][2]):
                continue
            srt_arr_eiv[i][2] = True
            j = srt_arr_eiv[i][1]
            while (not srt_arr_eiv[j][2]):
                srt_arr_eiv[j][2] = True
                swaps += 1
                j = srt_arr_eiv[j][1]
        return swaps
