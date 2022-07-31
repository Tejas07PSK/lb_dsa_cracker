class Solution:
    def __addAtBottom (self, stk, element)
        if (stk):
            curr_ele = stk.pop()
            self.__addAtBottom(stk)
            stk.append(curr_ele)
        else: stk.append(element)

    def reverse (self, stk):
        if (not stk): return
        element = stk.pop()
        self.reverse(stk)
        self.__addAtBottom(stk, element)
