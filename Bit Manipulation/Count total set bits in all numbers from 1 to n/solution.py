class Solution:
    def countBits (self, N):
        set_bits = 0
        while (N > 0):
            mx_pwr_2_lt_n, mx_pwr_2_lt_n_val = 0, 1
            while ((mx_pwr_2_lt_n_val << 1) <= N):
                mx_pwr_2_lt_n_val <<= 1 ; mx_pwr_2_lt_n += 1
            set_bits += (((mx_pwr_2_lt_n_val >> 1) * mx_pwr_2_lt_n) + (N - mx_pwr_2_lt_n_val + 1))
            N -= mx_pwr_2_lt_n_val
        return set_bits
