class Solution:
    def merge (self, l1, r1, l2, r2, mx_val, arr):
        i, j, k = l1, l2, l1
        while ((i <= r1) and (j <= r2)):
            if ((arr[i] % mx_val) > (arr[j] % mx_val)):
                arr[k] += (arr[j] % mx_val) * mx_val
                j += 1
            else:
                arr[k] += (arr[i] % mx_val) * mx_val
                i += 1
            k += 1
        while (i <= r1):
            arr[k] += (arr[i] % mx_val) * mx_val
            i += 1
            k += 1
        while (j <= r2):
            arr[k] += (arr[j] % mx_val) * mx_val
            j += 1
            k += 1
        k = l1
        while (k <= r2):
            arr[k] //= mx_val
            k += 1

    def mergeSortInPlace (self, l, r, mx_val, arr):
        sz = r - l + 1
        if (sz < 2): return
        elif (sz == 2):
            if (arr[l] > arr[r]): arr[l], arr[r] = arr[r], arr[l]
        else:
            mid = l + ((r - l) // 2)
            self.mergeSortInPlace(l, mid, mx_val, arr)
            self.mergeSortInPlace(mid + 1, r, mx_val, arr)
            self.merge(l, mid, mid + 1, r, mx_val, arr)

arr = [7, 7, 3, 1, 2, 3, 3, 4, 13, 9, 8, 9, 10, 1]
mx_val = max(arr) + 1
Solution().mergeSortInPlace(0, len(arr) - 1, mx_val, arr)
print(arr)
     