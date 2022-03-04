'''
class Node:
    def __init__(self):
        self.data = None
        self.next = None
'''

class Solution:
    def splitList (self, head, head1, head2):
        fast_ptr, slow_ptr = head, head
        while ((fast_ptr.next != head) and (fast_ptr.next.next != head)):
            slow_ptr, fast_ptr = slow_ptr.next, fast_ptr.next.next
        if (fast_ptr.next == head): fast_ptr.next = slow_ptr.next
        else: fast_ptr.next.next = slow_ptr.next
        head1, head2 = head, slow_ptr.next
        slow_ptr.next = head1
        return head1, head2
