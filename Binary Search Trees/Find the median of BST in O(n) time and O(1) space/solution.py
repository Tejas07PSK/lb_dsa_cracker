# Tree Node
# class Node:
#     def __init__(self, val):
#         self.right = None
#         self.data = val
#         self.left = None

def findMedian(root):
    ptr, n = root, 0
    while (ptr != None):
        if (ptr.left == None): n, ptr = n + 1, ptr.right
        else:
            temp = ptr.left
            while ((temp.right != None) and (temp.right != ptr)): temp = temp.right
            if (temp.right == None): temp.right, ptr = ptr, ptr.left
            else: temp.right, n, ptr = None, n + 1, ptr.right
    flag = ((n % 2) == 0)
    med_eles, k, ptr, n = [0, 0], ((n // 2) + 1), root, 0
    while (ptr != None):
        if (ptr.left == None):
            n += 1
            if (n <= k): med_eles[0], med_eles[1] = med_eles[1], ptr.data
            ptr = ptr.right
        else:
            temp = ptr.left
            while ((temp.right != None) and (temp.right != ptr)): temp = temp.right
            if (temp.right == None): temp.right, ptr = ptr, ptr.left
            else:
                temp.right, n = None, n + 1
                if (n <= k): med_eles[0], med_eles[1] = med_eles[1], ptr.data
                ptr = ptr.right
    median = med_eles[1]
    if (flag):
        median += med_eles[0]
        median = (median // 2) if ((median % 2) == 0) else (median / 2)
    return median
