class Solution:
    def productExceptSelf (self, arr, n):
        left_right_res = [[1 for i in range(n)] for i in range(2)]
        prev_left, prev_right, i, j = 1, 1, 0, n - 1
        while (i < n):
            left_right_res[0][i] = prev_left ; left_right_res[1][j] = prev_right
            prev_left *= arr[i] ; prev_right *= arr[j]
            i += 1 ; j -= 1
        i = 0
        while (i < n):
            right = left_right_res[1][i]
            left_right_res[1][i] = left_right_res[0][i] * right
            i += 1
        return left_right_res[1]
