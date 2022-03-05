'''
        # Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
'''

class Solution:
    def isPalindrome (self, head):
        slow_ptr, fast_ptr = head, head
        while ((fast_ptr.next != None) and (fast_ptr.next.next != None)):
            slow_ptr, fast_ptr = slow_ptr.next, fast_ptr.next.next
        end_flag = False
        if (fast_ptr.next == None): end_flag = True
        prev, curr, after = None, slow_ptr.next, None
        while (curr != None):
            after = curr.next ; curr.next = prev
            prev = curr ; curr = after
        slow_ptr.next = prev
        head2 = slow_ptr.next
        end1 = slow_ptr if end_flag else slow_ptr.next
        while (head != end1):
            if (head.data != head2.data): return False
            head, head2 = head.next, head2.next
        return True
