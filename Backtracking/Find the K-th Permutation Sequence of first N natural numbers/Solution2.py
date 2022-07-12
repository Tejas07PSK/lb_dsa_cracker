class Solution:
    def getPermutation (self, n: int, k: int) -> str:
        fact_list, num_lst = [1 for i in range(n)], [str(i) for i in range(1, n + 1)]
        res = [] ; k -= 1
        for i in range(1, n): fact_list[i] = i * fact_list[i - 1]
        while (len(num_lst) > 0):
            idx = k // fact_list[len(num_lst) - 1]
            res.append(num_lst[idx])
            k %= fact_list[len(num_lst) - 1]
            num_lst.pop(idx)
        return "".join(res)
