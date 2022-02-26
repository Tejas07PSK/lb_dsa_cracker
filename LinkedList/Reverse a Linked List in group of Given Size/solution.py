class Solution:
    def reverse (self, ll_head, k):
        if ((ll_head == None) or (k == 1)): return ll_head
        prev_start, start = None, None
        prev, curr, after, start = None, ll_head, None, None
        i, cnt = 0, 0
        while (curr != None):
            i += 1
            if (i == 1):
                prev_start = start ; start = curr
                prev = curr ; curr = curr.next
            else: 
                if (i == k):
                    if (cnt == 0):
                        ll_head = curr ; cnt += 1
                    if (prev_start != None): prev_start.next = curr
                    i = 0
                after = curr.next ; curr.next = prev ; prev = curr; curr = after
        start.next = None
        if (i < k):
            if (cnt == 0):
                ll_head = prev ; cnt += 1
            if (prev_start != None): prev_start.next = prev
        return ll_head
