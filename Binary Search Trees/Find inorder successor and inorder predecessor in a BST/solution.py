'''
  	Following is the Binary Tree node structure:
	class BinaryTreeNode:
	    def __init__(self, data):
	        self.data = data
	        self.left = None
	        self.right = None
'''

def findPreSuc (root, key):
	if (root == None): return [-1, -1]
	ptr, res = root, [-1, -1]
	while (ptr != None):
		if (key == ptr.data):
			if (ptr.left != None):
                ptr_in_pred = ptr.left
				while (ptr_in_pred.right != None): ptr_in_pred = ptr_in_pred.right
				res[0] = ptr_in_pred.data
			if (ptr.right != None):
                ptr_in_succ = ptr.right
				while (ptr_in_succ.left != None): ptr_in_succ = ptr_in_succ.left
				res[1] = ptr_in_succ.data
			return res
		elif (key < ptr.data): res[1], ptr = ptr.data, ptr.left
		else: res[0], ptr = ptr.data, ptr.right
	return [-1, -1]
