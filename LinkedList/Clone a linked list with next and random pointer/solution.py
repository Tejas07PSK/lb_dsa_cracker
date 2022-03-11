'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.arb=None
'''

class Solution:
    def copyList (self, head):
        prev, curr = None, head
        while (curr != None):
            prev = curr ; curr = curr.next
            prev.next = Node(prev.data)
            prev.next.next = curr
        curr = head
        while (curr != None):
            if (curr.arb != None):
                curr.next.arb = curr.arb.next
            curr = curr.next.next
        prev, curr, head_new, prev_new = None, head, None, None
        while (curr != None):
            prev = curr ; curr = curr.next.next
            if (prev_new == None):
                head_new = prev.next ; prev_new = prev.next
            else:
                prev_new.next = prev.next ; prev_new = prev_new.next
            prev_new.next = None ; prev.next = curr
        return head_new
