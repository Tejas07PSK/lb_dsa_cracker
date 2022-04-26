from collections import deque
from heapq import heappush, heappop

class TreeNode:
    def __init__ (self, freq, ch=""):
        self.ch, self.freq = ch, freq
        self.left, self.right = None, None

    def __lt__ (self, other): return (self.freq < other.freq)

class Solution:
    def __preOrderTraverser (self, tree_root, char_code_list, bit_stream):
        if (tree_root.ch != ""): char_code_list.append("".join(bit_stream))
        if (tree_root.left != None):
            bit_stream.append('0') ; self.__preOrderTraverser(tree_root.left, char_code_list, bit_stream) ; bit_stream.pop()
        if (tree_root.right != None):
            bit_stream.append('1') ; self.__preOrderTraverser(tree_root.right, char_code_list, bit_stream) ; bit_stream.pop()

    def huffmanCodes (self, S, f, N):
        min_heap, char_code_list = [], []
        for i in range(N): heappush(min_heap, TreeNode(f[i], S[i]))
        while (len(min_heap) > 1):
            left_node, right_node = heappop(min_heap), heappop(min_heap)
            root = TreeNode((left_node.freq + right_node.freq))
            root.left, root.right = left_node, right_node ; heappush(min_heap, root)
        tree_root = heappop(min_heap) ; self.__preOrderTraverser(tree_root, char_code_list, deque())
        return char_code_list
