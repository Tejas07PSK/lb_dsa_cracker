def insertAtBottom (stk, element):
    if (stk):
        curr_top = stk.pop()
        insertAtBottom(stk, element)
        stk.append(curr_top)
    else: stk.append(element)
