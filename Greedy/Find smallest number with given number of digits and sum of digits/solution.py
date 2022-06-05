class Solution:
    def smallestNumber (self, S, D):
        if ((9 * D) < S): return "-1"
        number = [None for i in range(D)]
        i = D - 1
        while (S > 9): number[i], S, i = '9', S - 9, i - 1
        if (i == 0): number[i] = str(S)
        else:
            number[i], i = str(S - 1), i - 1
            while (i > 0): number[i], i = '0', i - 1
            number[i] = '1'
        return "".join(number)
