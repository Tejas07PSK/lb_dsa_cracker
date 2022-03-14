class ListNode:
    def __init__ (self, data):
        self.data = data
        self.prev = None
        self.next = None

class Solution:
    def FirstNonRepeating (self, A):
        hm = {} ; head, tail = None, None
        res = []
        for ch in A:
            if (ch not in hm):
                if (tail == None):
                    tail = ListNode(ch) ; head = tail
                else:
                    tail.next = ListNode(ch) ; tail.next.prev = tail ; tail = tail.next
                hm[tail.data] = tail
            elif ((hm[ch].prev != None) or (hm[ch].next != None)):
                if (hm[ch] == head):
                    head.next.prev = None ; head = head.next ; hm[ch].next = None
                elif (hm[ch] == tail):
                    tail.prev.next = None ; tail = tail.prev ; hm[ch].prev = None
                else:
                    hm[ch].prev.next = hm[ch].next ; hm[ch].next.prev = hm[ch].prev
                    hm[ch].prev, hm[ch].next = None, None
            elif (hm[ch] == head): head, tail = None, None
            res.append(head.data if head != None else '#')
        return "".join(res)
