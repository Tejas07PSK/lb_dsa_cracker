class Solution:
    def  sortBySetBitCount (self, arr, n):
        arr.sort(key=lambda x : x.bit_count())
