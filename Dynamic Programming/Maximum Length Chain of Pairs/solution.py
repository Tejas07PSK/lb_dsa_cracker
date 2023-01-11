'''
class Pair (object):
    def __init__ (self, a, b):
        self.a = a
        self.b = b
'''

class Solution:
    def maxChainLen (self, parr, n):
        parr.sort(key=lambda x: x.b)
        prev_num = parr[0].b
        sz = 1
        for i in range(1, len(parr)):
            if (prev_num < parr[i].a):
                sz += 1
                prev_num = parr[i].b
        return sz
