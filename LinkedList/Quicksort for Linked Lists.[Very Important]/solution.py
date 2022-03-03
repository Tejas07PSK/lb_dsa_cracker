def __partition (head, end):
    i, i_prev, j, j_prev, pvt = head, None, head, None, end.data
    while (i != end):
        if (i.data < pvt):
            temp1, temp2 = j.next, i.next
            if (j_prev != None): j_prev.next = i
            else: head = i
            j.next = temp2
            if (temp1 == i): i.next = j
            else:
                i.next = temp1
                if (i_prev != None): i_prev.next = j
            i, j = j, i
            j_prev, j = j, j.next
            i_prev, i = i, i.next
        else: i_prev, i = i, i.next
    temp1, temp2 = j.next, i.next
    if (j_prev != None): j_prev.next = i
    else: head = i
    j.next = temp2
    if (temp1 == i): i.next = j
    else:
        i.next = temp1
        if (i_prev != None): i_prev.next = j
    i, j = j, i ; end = i
    return head, j_prev, j, end
        
def __quickSortHelper (head, end):
    if (head == end): return head, end
    if (head.next == end):
        if (end.data < head.data):
            temp = end.next ; end.next = head
            head.next = temp ; head, end = end, head
        return head, end
    head, pivot_prev, pivot, end = __partition(head, end)
    if (pivot_prev != None): head, pivot_prev = __quickSortHelper(head, pivot_prev)
    if (pivot.next != end.next): pivot.next, end = __quickSortHelper(pivot.next, end)
    return head, end

def quickSort (head):
    if (head == None): return head
    curr = head
    while (curr.next != None): curr = curr.next
    head, end = __quickSortHelper(head, curr)
    return head
