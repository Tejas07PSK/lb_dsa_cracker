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

    def addTwoLists (self, head1, head2):
        head1, head2 = self.reverseLinkedList(head1), self.reverseLinkedList(head2)
        new_head, curr1, curr2, prev, carry = None, head1, head2, None, 0
        while ((curr1 != None) and (curr2 != None)):
            temp = curr1.data + curr2.data + carry
            carry = temp // 10 ; curr1 = curr1.next ; curr2 = curr2.next
            if (prev != None):
                prev.next = Node(temp % 10) ; prev = prev.next
            else:
                prev = Node(temp % 10) ; new_head = prev
        while (curr1 != None):
            temp = curr1.data + carry ; carry = temp // 10 ; curr1 = curr1.next
            prev.next = Node(temp % 10) ; prev = prev.next
        while (curr2 != None):
            temp = curr2.data + carry ; carry = temp // 10 ; curr2 = curr2.next
            prev.next = Node(temp % 10) ; prev = prev.next
        if (carry != 0): prev.next = Node(carry)
        return self.reverseLinkedList(new_head)
