"""Return reference of new head of the reverse linked list
  The input list will have at least one element
  Node is defined as

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
  This is method only submission.
  You only need to complete the method.
"""
class Solution:
    def reverse (self, ll_head, k):
        if ((ll_head == None) or (k == 1)): return ll_head
        prev, curr, after, i = None, ll_head, None, 1
        while ((curr != None) and (i <= k)):
            after = curr.next ; curr.next = prev
            prev = curr ; curr = after ; i += 1
        prev_start, start = ll_head, curr
        ll_head = prev ; prev = None ; i = 1
        while (curr != None):
            if ((i == k) or (curr.next == None)):
                prev_start.next = curr ; after = curr.next
                curr.next = prev ; prev = None
                curr = after ; i = 1
                prev_start = start ; start = curr
            else:
                after = curr.next ; curr.next = prev
                prev = curr ; curr = after ; i += 1
        return ll_head
