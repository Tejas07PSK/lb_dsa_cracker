'''
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

class Solution:
    def reverseLinkedList (self, head):
        prev, curr, after = None, head, None
        while (curr != None):
            after = curr.next ; curr.next = prev
            prev = curr ; curr = after
        head = prev
        return head

    def addOne (self, head):
        head = self.reverseLinkedList(head) ; prev, curr = None, head
        carry = 1
        while ((curr != None) and (carry != 0)):
            temp = curr.data + carry ; curr.data = temp % 10
            carry = temp // 10 ; prev = curr ; curr = curr.next
        if (carry != 0): prev.next = Node(carry)
        return self.reverseLinkedList(head)
