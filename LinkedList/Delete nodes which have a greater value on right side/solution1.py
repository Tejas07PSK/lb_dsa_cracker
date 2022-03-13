'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''

class Solution:
    def __reverse (self, head):
        prev, curr, after = None, head, None
        while (curr != None):
            after = curr.next ;curr.next = prev
            prev = curr ; curr = after
        head = prev ; return head

    def compute (self, head):
        head = self.__reverse(head)
        mx_so_far = head.data ; curr = head
        while (curr.next != None):
            if (curr.next.data < mx_so_far):
                temp = curr.next
                curr.next = curr.next.next
                temp.next = None
            else:
                mx_so_far = curr.next.data
                curr = curr.next
        head = self.__reverse(head) ; return head
