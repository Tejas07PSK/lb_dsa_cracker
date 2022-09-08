'''
class Node:
    def __init__(self,x):
        self.data = x
        self.next = None
'''
from heapq import heapify, heappop, heappush
class Solution:
    def mergeKLists (self, arr, K):
        hp = [(start.data, id(start), start) for start in arr]
        prev, start, curr = None, None, None
        heapify(hp)
        while (hp):
            val, id_val, curr = heappop(hp)
            if (curr.next != None): heappush(hp, (curr.next.data, id(curr.next), curr.next))
            curr.next = None
            if (prev != None):
                prev.next = curr
                prev = prev.next
            else: start = prev = curr
        return start
