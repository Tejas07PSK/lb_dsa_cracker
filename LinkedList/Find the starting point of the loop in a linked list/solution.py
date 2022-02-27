# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head == None): return None
        slow_ptr, fast_ptr = head, head
        while ((slow_ptr.next != None) and (fast_ptr.next != None) and (fast_ptr.next.next != None)):
            slow_ptr = slow_ptr.next ; fast_ptr = fast_ptr.next.next
            if (slow_ptr == fast_ptr):
                slow_ptr = head
                while (slow_ptr != fast_ptr):
                    slow_ptr = slow_ptr.next ; fast_ptr = fast_ptr.next
                return slow_ptr
        return None
