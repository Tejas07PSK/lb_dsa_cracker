class Solution:
    def JobScheduling (self, N, Jobs):
        Jobs.sort(key=lambda x: x[1]) ; max_profit = Jobs[0][2] ; profit_calc_arr = [Jobs[i][2] for i in range(N)]
        for i in range(1, N):
            for j in range(0, i):
                if (Jobs[j][1] < Jobs[i][0]): profit_calc_arr[i] = max(profit_calc_arr[i], (profit_calc_arr[j] + Jobs[i][2]))
            max_profit = max(max_profit, profit_calc_arr[i])
        return max_profit
