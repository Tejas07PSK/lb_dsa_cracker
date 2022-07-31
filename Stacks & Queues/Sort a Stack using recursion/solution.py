class Solution:
    def __sortedInsert (self, stk, element):
        if (stk):
            if (element < stk[-1]):
                curr_ele = stk.pop()
                self.__sortedInsert(stk, element)
                stk.append(curr_ele)
            else: stk.append(element)
        else: stk.append(element)

    def sorted (self, s):
        if (not s): return
        element = s.pop()
        self.sorted(s)
        self.__sortedInsert(s, element)
