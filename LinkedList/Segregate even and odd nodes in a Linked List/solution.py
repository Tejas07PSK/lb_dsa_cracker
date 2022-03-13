# Following is the structure of node 
# class Node:
#     def __init__(self):  
#         self.data = None
#         self.next = None

class Solution:
    def divide (self, N, head):
        tail_even, head_odd, tail_odd, ptr = None, None, None, head
        while (ptr != None):
            temp = ptr ; ptr = ptr.next
            if ((temp.data % 2) == 0):
                if (tail_even == None): head = temp
                else: tail_even.next = temp
                tail_even = temp ; tail_even.next = None
            else:
                if (tail_odd == None): head_odd = temp
                else: tail_odd.next = temp
                tail_odd = temp ; tail_odd.next = None
        if (tail_even != None):
            tail_even.next = head_odd
        return head
