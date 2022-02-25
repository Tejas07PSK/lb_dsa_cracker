# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr, after = None, head, None
        while (curr != None):
            after = curr.next ; curr.next = prev
            prev = curr ; curr = after
        head = prev
        return head
