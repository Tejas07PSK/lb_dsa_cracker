class Solution:
    __roman_symbol_to_dec_table = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    def romanToDecimal (self, rom_str):
        i = len(rom_str) - 1
        prev_sym_val = Solution.__roman_symbol_to_dec_table[rom_str[i]]
        num = prev_sym_val
        i -= 1
        while (i >= 0):
            curr_sym_val = Solution.__roman_symbol_to_dec_table[rom_str[i]]
            if (curr_sym_val >= prev_sym_val):
                num += curr_sym_val
            else:
                num -= curr_sym_val
            prev_sym_val = curr_sym_val
            i -= 1
        return num
