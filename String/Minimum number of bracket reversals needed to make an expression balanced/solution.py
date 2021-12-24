class Solution:
    def countRev (self, S):
        cons_open_braces, cons_close_braces = 0, 0
        for brac in S:
            if (brac == '{'):
                cons_open_braces += 1
            elif (brac == '}'):
                if (cons_open_braces > 0):
                    cons_open_braces -= 1
                else:
                    cons_close_braces += 1
        if ((cons_open_braces == 0) and (cons_close_braces == 0)):
            return 0
        rem_open, rem_close = cons_open_braces % 2, cons_close_braces % 2
        quo_open, quo_close = cons_open_braces // 2, cons_close_braces // 2
        if (rem_open != rem_close):
            return -1
        return (quo_open + rem_open + quo_close + rem_close)
