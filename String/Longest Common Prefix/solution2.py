class Solution:
    def __find_min_len_str_in_list (self, strs, n):
        min_idx, min_len = 0, len(strs[0])
        for i in range(1, n):
            curr_len = len(strs[i])
            if (curr_len < min_len):
                min_len = curr_len
                min_idx = i
        return min_idx, min_len

    def __search_in_list_after_first (self, strs, n, lcp):
        for i in range(1, n):
            if (not strs[i].startswith(lcp)):
                return False
        return True

    def longestCommonPrefix (self, strs: List[str]) -> str:
        n = len(strs)
        if (n == 0):
            return ""
        if (n == 1):
            return strs[0]
        min_idx, min_len = self.__find_min_len_str_in_list(strs, n)
        strs[0], strs[min_idx] = strs[min_idx], strs[0]
        low, high = 0, min_len - 1
        lcp, ans = "", ""
        while (low <= high):
            mid = low + ((high - low) // 2)
            lcp = strs[0][0:(mid + 1)]
            if (self.__search_in_list_after_first(strs, n, lcp)):
                low = mid + 1
                ans = lcp
            else:
                lcp = ""
                high = mid - 1
        return ans
