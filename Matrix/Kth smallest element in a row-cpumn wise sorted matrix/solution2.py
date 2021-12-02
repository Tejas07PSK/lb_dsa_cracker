def count_eles_lt_point (mat, N, point):
    row, c = 0, 0
    while (row < N):
        left, right = 0, (N - 1)
        while (left <= right):
            mid = left + ((right - left) // 2)
            if (mat[row][mid] > point):
                right = mid - 1
            else:
                left = mid + 1
        c += left
        row += 1
    return c

def kthSmallest (mat, N, K):
    start, end = mat[0][0], mat[N - 1][N - 1]
    while (start <= end):
        point = start + ((end - start) // 2)
        c = count_eles_lt_point(mat, N, point)
        if (c >= K):
            end = point - 1
        else:
            start = point + 1
    return start
