class Solution:
    def minimumNumberOfSwaps (self, string):
        i, j, n = 0, 0, len(string)
        ans, balance, offset = 0, 0, 0
        while ((i < n) and (j < n)):
            if (i == j):
                balance, offset = 0, 0
            if (string[i] == '['):
                if (balance >= 0):
                    balance += 1
                else:
                    offset -= 1
            if (string[i] == ']'):
                if (balance >= 0):
                    balance -= 1
                if (balance < 0):
                    if (j <= i):
                        j = i + 1
                    while ((string[j] != '[') and (j < n)):
                        j += 1
                    ans += j - (i + offset)
                    offset += 1
                    j += 1
            i += 1
        return ans
