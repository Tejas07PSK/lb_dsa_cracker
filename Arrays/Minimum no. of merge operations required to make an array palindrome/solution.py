class Solution:
    def min_merge_ops_to_make_arr_palin (self, arr, n):
        i, j = 0, n - 1
        moves = 0
        while (i < j):
            if (arr[i] == arr[j]):
                i += 1 ; j -= 1
            elif (arr[i] > arr[j]):
                arr[j - 1] += arr[j]
                j -= 1
                moves += 1
            else:
                arr[i + 1] += arr[i]
                i += 1
                moves += 1
        return moves

arr = [15, 4, 15]
print(Solution().min_merge_ops_to_make_arr_palin(arr, len(arr)))

arr = [1, 4, 5, 1]
print(Solution().min_merge_ops_to_make_arr_palin(arr, len(arr)))

arr = [11, 14, 15, 99]
print(Solution().min_merge_ops_to_make_arr_palin(arr, len(arr)))
