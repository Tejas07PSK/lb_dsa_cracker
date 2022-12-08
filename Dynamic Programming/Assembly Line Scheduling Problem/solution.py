class Solution:
    def assembly_line_scheduling (self,
                                   static_station_time_mat,
                                   diagonal_station_chg_time_mat,
                                   lines_start_end_times_mat, lines, stations):
        dp = [[0 for j in range(stations)] for i in range(lines)]
        for i in range(lines):
            dp[i][0] = lines_start_end_times_mat[i][0]
            dp[i][stations - 1] = lines_start_end_times_mat[i][1]
        for j in range(stations - 1, -1, -1):
            for i in range(lines - 1, -1, -1):
                dp[i][j] += static_station_time_mat[i][j]
                mn_frm_right = 0
                if ((j + 1) <= (stations - 1)):
                    mn_frm_right = dp[i][j + 1]
                    if ((i - 1) >= 0):
                        mn_frm_right = min(mn_frm_right,
                                           (diagonal_station_chg_time_mat[i][j][0]
                                            + dp[i - 1][j + 1]))
                    if ((i + 1) <= (lines - 1)):
                        mn_frm_right = min(mn_frm_right,
                                           (diagonal_station_chg_time_mat[i][j][1]
                                            + dp[i + 1][j + 1]))
                dp[i][j] += mn_frm_right
        ans = dp[0][0]
        for i in range(1, lines): ans = min(ans, dp[i][0])
        return ans

static_staion_time_mat = [[4, 5, 3, 2],
                          [2, 10, 1, 4]]
diagonal_station_chg_time_mat = [[(0, 7), (0, 4), (0, 5), (0, 0)],
                                 [(9, 0), (2, 0), (8, 0), (0, 0)]]
lines_start_end_times_mat = [[10, 18],
                             [12, 7]]
lines, stations = 2, 4
print(Solution().assembly_line_scheduling(static_staion_time_mat,
                                            diagonal_station_chg_time_mat,
                                            lines_start_end_times_mat, lines, stations))
