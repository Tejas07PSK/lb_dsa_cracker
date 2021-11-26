class Solution:
    def create_temp_arr (self, Mat, start, end, N):
        arr = []
        while (start <= end):
            j = 0
            while (j < N):
                arr.append(Mat[start][j])
                j += 1
            start += 1
        return arr

    def fill_rem_elements (self, Mat, i, j, arr, idx, arr_len, N):
        while (idx < arr_len):
            Mat[i][j] = arr[idx]
            idx += 1
            j += 1 ; j %= N ; i = (i + 1) if (j == 0) else i
        return i, j

    def merge (self, Mat, l, mid, r, N):
        left_arr = self.create_temp_arr(Mat, l, mid, N)
        right_arr = self.create_temp_arr(Mat, (mid + 1), r, N)
        l_idx, r_idx, left_arr_len, right_arr_len = 0, 0, len(left_arr), len(right_arr)
        i, j = l, 0
        while ((l_idx < left_arr_len) and (r_idx < right_arr_len)):
            if (left_arr[l_idx] < right_arr[r_idx]):
                Mat[i][j] = left_arr[l_idx]
                l_idx += 1
            elif (left_arr[l_idx] > right_arr[r_idx]):
                Mat[i][j] = right_arr[r_idx]
                r_idx += 1
            else:
                Mat[i][j] = left_arr[l_idx]
                l_idx += 1
                j += 1 ; j %= N ; i = (i + 1) if (j == 0) else i
                Mat[i][j] = right_arr[r_idx]
                r_idx += 1
            j += 1 ; j %= N ; i = (i + 1) if (j == 0) else i
        i, j = self.fill_rem_elements(Mat, i, j, left_arr, l_idx, left_arr_len, N)
        i, j = self.fill_rem_elements(Mat, i, j, right_arr, r_idx, right_arr_len, N)

    def sortedMatrix (self, Mat, N):
        self.merge_sort_matrix(Mat, 0, (N - 1), N)

    def merge_sort_matrix (self, Mat, l, r, N):
        size = r - l + 1
        if (size < 2):
            return
        mid = l + ((r - l) // 2)
        self.merge_sort_matrix(Mat, l, mid, N)
        self.merge_sort_matrix(Mat, (mid + 1), r, N)
        self.merge(Mat, l, mid, r, N)
