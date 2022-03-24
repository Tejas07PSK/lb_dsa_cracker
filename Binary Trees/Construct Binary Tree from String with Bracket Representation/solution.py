import io, os, sys
from collections import deque
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

class TreeNode:
    def __init__ (self, data): self.data, self.left, self.right = data, None, None

class Solution:
    def __inorderTraverseTree (self, root, res):
        if (root == None): return res
        res.append(root.data)
        if (root.left != None): self.__inorderTraverseTree(root.left, res)
        if (root.right != None): self.__inorderTraverseTree(root.right, res)

    def __constructTree (self, inp_string):
        stk = deque() ; i = 0 ; n = len(inp_string)
        while (i < n):
            if (inp_string[i] == '('):
                if (inp_string[i + 1] == ')'): i += 2
                else: i += 1
            elif (inp_string[i] == ')'):
                node = stk.pop() ; i += 1
                if (stk[-1].left != None): stk[-1].right = node
                else: stk[-1].left = node
            else:
                stk.append(TreeNode(inp_string[i])) ; i += 1
        return stk.pop()

    def main (self):
        inp_string = input().decode()
        root = self.__constructTree(inp_string) ; res = deque()
        self.__inorderTraverseTree(root, res)
        sys.stdout.write(str(res) + '\n')

Solution().main()
