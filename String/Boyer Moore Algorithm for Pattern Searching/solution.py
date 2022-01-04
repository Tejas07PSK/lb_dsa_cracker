class Solution:
    def __create_Z_array (self, string, n):
        Z = [0 for i in range(n)]
        left, right = 0, 0
        for k in range(1, n):
            if (k > right):
                left, right = k, k
                while ((right < n) and (string[right] == string[right - left])):
                    right += 1
                Z[k] = right - left
                right -= 1
            else:
                x = k - left
                if ((Z[x] + k - 1) < right):
                    Z[k] = Z[x]
                else:
                    left = k
                    while ((right < n) and (string[right] == string[right - left])):
                        right += 1
                    Z[k] = right - left
                    right -= 1
        return Z

    def __create_good_suffix_arrays (self, string, n):
        N = self.__create_Z_array(string[::-1], n) ; N.reverse() ; print(N)
        L = [0 for i in range(n + 1)]
        l = [0 for i in range(n + 1)]
        for j in range(n):
            i = n - N[j]
            L[i] = j
        r_k, k = n, 0
        for j in range(n):
            k = j if (N[j] == j + 1) else k
            l[r_k] = k
            r_k -= 1
        return L, l

    def __create_bad_char_map (self, string, n):
        R = {}
        for i in range(n):
            R[string[i]] = i
        return R

    def searchBM (self, text, string):
        m, n = len(text), len(string)
        k = n - 1
        R = self.__create_bad_char_map(string, n)
        L, l = self.__create_good_suffix_arrays(string, n)
        print((R,L,l))
        while (k < m):
            i, h = n - 1, k
            while ((i >= 0) and (string[i] == text[h])):
                i -= 1 ; h -= 1
            if (i == -1):
                print("starts at = " + str(h+1))
                k += n - 1 - l[1]
            else:
                k += max(1, i - (R[text[h]] if text[h] in R else -1), n - 1 - (L[i + 1] if L[i + 1] != 0 else l[i + 1]))
