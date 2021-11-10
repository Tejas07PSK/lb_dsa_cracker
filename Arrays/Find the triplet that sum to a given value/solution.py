class Solution:
    def find3Numbers (self, arr, n, x):
        arr.sort()
        res = False
        for i in range(0, (n - 2)):
            two_sum = (x - arr[i])
            j, k = (i + 1), (n - 1)
            while (j < k):
                temp_sum = (arr[j] + arr[k])
                if (temp_sum < two_sum):
                    j += 1
                elif (temp_sum > two_sum):
                    k -= 1
                else:
                    res = True
                    break
            if (res == True):
                break
        return (res)
