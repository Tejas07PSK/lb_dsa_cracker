from math import inf
def buildHeap (arr, n):
    # use heapify algorithm
    for i in range((n - 1), -1, -1):
        curr_idx, curr_ele = i, arr[i]
        left_idx, right_idx = 2 * i + 1, 2 * i + 2
        left_ele = arr[left_idx] if (left_idx < n) else -inf
        right_ele = arr[right_idx] if (right_idx < n) else -inf
        while (not ((curr_ele >= left_ele) and (curr_ele >= right_ele))):
            if (right_ele > left_ele):
                arr[curr_idx], arr[right_idx] = right_ele, curr_ele
                curr_idx = right_idx
            else:
                arr[curr_idx], arr[left_idx] = left_ele, curr_ele
                curr_idx = left_idx
            curr_ele = arr[curr_idx]
            left_idx, right_idx = 2 * curr_idx + 1, 2 * curr_idx + 2
            left_ele = arr[left_idx] if (left_idx < n) else -inf
            right_ele = arr[right_idx] if (right_idx < n) else -inf
    return arr
