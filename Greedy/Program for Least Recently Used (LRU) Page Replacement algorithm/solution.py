class DLLNode:
    def __init__ (self, val): self.val, self.prev, self.next = val, None, None

class Solution:
    def pageFaults (self, N, C, pages):
        page_set, page_faults = {}, 0
        head, tail = None, None
        for i in range(N):
            if (pages[i] not in page_set):
                page_faults += 1
                if (len(page_set) == C):
                    tail.next = DLLNode(pages[i]) ; tail.next.prev = tail ; tail = tail.next ; page_set[pages[i]] = tail
                    del page_set[head.val] ; head = head.next ; head.prev.next = None ; head.prev = None
                else:
                    if (head == None): head = tail = DLLNode(pages[i])
                    else:
                        tail.next = DLLNode(pages[i]) ; tail.next.prev = tail ; tail = tail.next
                    page_set[pages[i]] = tail
            else:
                tail.next = DLLNode(pages[i]) ; tail.next.prev = tail ; tail = tail.next
                node = page_set[pages[i]]
                page_set[pages[i]] = tail
                if (node == head):
                    head = head.next ; head.prev.next = None ; head.prev = None
                else:
                    node.prev.next = node.next ; node.next.prev = node.prev
                    node.next, node.prev = None, None
        return page_faults
