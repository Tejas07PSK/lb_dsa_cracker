# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def recursiveHelper (self, prev, curr):
        if (curr == None):
            return prev
        end = self.recursiveHelper(curr, curr.next)
        curr.next = prev ; return end

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = self.recursiveHelper(None, head)
        return head
