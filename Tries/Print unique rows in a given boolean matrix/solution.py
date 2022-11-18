class TrieNode:
    def __init__ (self):
        self.children = {}
        self.is_end = False

def uniqueRow (row, col, matrix):
    root, res = TrieNode(), []
    matrix = [[matrix[j] for j in range(i, i + col)] for i in range(0, len(matrix), col)]
    for row in matrix:
        ptr = root
        for item in row:
            if (item not in ptr.children): ptr.children[item] = TrieNode()
            ptr = ptr.children[item]
        if (not ptr.is_end):
            res.append(row)
            ptr.is_end = True
    return res
