class Solution:
    def countAndSay(self, n: int) -> str:
        prev_str = "1"
        i = 2
        while (i <= n):
            j = 0
            intr_res = []
            psl = len(prev_str)
            cntr = 0
            while (j < psl):
                cntr += 1
                if ((((j + 1) < psl) and (prev_str[j] != prev_str[j + 1])) or (j == (psl - 1))):
                    intr_res.append(str(cntr) + prev_str[j])
                    cntr = 0
                j += 1
            prev_str = "".join(intr_res)
            i += 1
        return prev_str
