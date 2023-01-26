def __liss_helper (root):
    take, not_take = 1, 0
    if (root.left != None):
        take_from_left, not_take_from_left, mx_sz_from_left = __liss_helper(root.left)
        take += not_take_from_left
        not_take += max(not_take_from_left, take_from_left)
    if (root.right != None):
        take_from_right, not_take_from_right, mx_sz_from_right = __liss_helper(root.right)
        take += not_take_from_right
        not_take += max(not_take_from_right, take_from_right)
    return take, not_take, max(take, not_take)

def LISS (root): return __liss_helper(root)[2]
