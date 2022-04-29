def maxStop (trains, n, m):
    platform_dep_times_array, res = [-1 for i in range(m + 1)], 0
    trains.sort(key=lambda x: x[0])
    for i in range(n):
        if (platform_dep_times_array[trains[i][2]] == -1): platform_dep_times_array[trains[i][2]], res = trains[i][1], res + 1
        elif (trains[i][0] >= platform_dep_times_array[trains[i][2]]): platform_dep_times_array[trains[i][2]], res = trains[i][1], res + 1
        else: platform_dep_times_array[trains[i][2]] = min(platform_dep_times_array[trains[i][2]], trains[i][1])
    return res
