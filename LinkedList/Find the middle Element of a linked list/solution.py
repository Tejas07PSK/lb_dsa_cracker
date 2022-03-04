# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head == None): return head
        slow_ptr, fast_ptr = head, head
        while ((fast_ptr.next != None) and (fast_ptr.next.next != None)):
            slow_ptr, fast_ptr = slow_ptr.next, fast_ptr.next.next
        if ((fast_ptr.next != None) and (fast_ptr.next.next == None)):
            slow_ptr = slow_ptr.next
        return slow_ptr
