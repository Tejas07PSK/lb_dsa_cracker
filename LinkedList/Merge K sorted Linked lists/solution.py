'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

from queue import PriorityQueue

class ListNodeWrapper:
    def __init__ (self, node): self.node = node
    def __lt__ (self, other): return (self.node.data < other.node.data)

class Solution:
    def mergeKLists (self, arr, k):
        q = PriorityQueue() ; curr, head = None, None
        for i in range(k):
            if (arr[i] != None): q.put((arr[i].data, ListNodeWrapper(arr[i])))
        while (not q.empty()):
            temp = q.get()[1]
            if (curr == None):
                curr = temp.node ; head = curr
            else:
                curr.next = temp.node ; curr = curr.next
            if (temp.node.next != None): q.put((temp.node.next.data, ListNodeWrapper(temp.node.next)))
        return head
