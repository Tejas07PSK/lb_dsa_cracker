class Solution:
    def __isPalindrome (self, string):
        i, j = 0, len(string) - 1
        while (i < j):
            if (string[i] != string[j]): return False
            i, j = i + 1, j - 1
        return True

    def __allPalindromicPermsHelper (self, string_so_far, string):
        if (string == ""):
            self.res.append(string_so_far.split()) ; return
        for i in range(1, len(string) + 1):
            prefix_str = string[0:i]
            if(self.__isPalindrome(prefix_str)):
                suffix_str = string[i:]
                ans = (prefix_str + " ") if (suffix_str != "") else prefix_str
                self.__allPalindromicPermsHelper(string_so_far + ans, suffix_str)

    def allPalindromicPerms (self, string):
        self.res = []
        self.__allPalindromicPermsHelper("", string)
        return self.res
