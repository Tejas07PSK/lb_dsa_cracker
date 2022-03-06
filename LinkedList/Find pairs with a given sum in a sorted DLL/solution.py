class ListNode:
    def __init__ (self, data):
        self.data, self.next, self.prev = data, None, None

class Solution:
    def __formSortedDll (self, arr, n):
        arr.sort() ; before, head = None, None
        for i in range(n):
            if (i == 0):
                before = ListNode(arr[i]) ; head = before
            else:
                before.next = ListNode(arr[i]) ; before.next.prev = before
                before = before.next
        return head, before

    def __printPairs (self, head, tail, k):
        if (head == None):
            print(None) ; return
        i, j = head, tail
        while ((j != i) or (j.next != i)):
            sum = i.data + j.data
            if (sum < k): i = i.next
            elif (sum > k): j = j.prev
            else: print((i.data, j.data))

    def __printList (self, head):
        while (head != None):
            print(head.data, end=' ') ; head = head.next
        print()

    def main (self):
        arr = [2, 5, 4, 9, 8, 1, 6] ; n = len(arr) ; k = 7
        head, tail = self.__formSortedDll(arr, n)
        self.__printList(head)
        self.__printPairs(head, tail, k)

Solution().main()
