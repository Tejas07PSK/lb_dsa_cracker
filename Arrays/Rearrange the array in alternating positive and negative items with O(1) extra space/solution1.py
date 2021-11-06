class Solution:
    def re_arrange (self, arr, n):
        for i in range(1, (n - 1)):
            val, tmp, idx, flag = "", 0, 0, 0
            if ((arr[i] < 0) and (arr[i - 1] < 0)):
                val = "next+"
            elif ((arr[i] > 0) and (arr[i - 1] > 0)):
                val = "next-"
            else:
                continue
            for j in range((i + 1), n):
                idx = j
                if ((val == "next+") and (arr[idx] > 0)):
                    flag = 1
                    break
                if ((val == "next-") and (arr[idx] < 0)):
                    flag = 1
                    break
            if (flag == 0):
                break
            temp = arr[idx]
            while (idx > i):
                arr[idx] = arr[idx - 1]
                idx -= 1
            arr[idx] = temp
 