class Solution:
    def factorial (self, n):
        if (n < 2):
            return [1]
        digits = [1]
        for i in range(2, (n + 1)):
            carry, product = 0, 0
            for j in range(-1, -(len(digits) + 1), -1):
                product = (digits[j] * i) + carry
                digits[j] = product % 10
                carry = product // 10
            while (carry > 0):
                digits.insert(0, (carry % 10))
                carry //= 10
        return (digits)